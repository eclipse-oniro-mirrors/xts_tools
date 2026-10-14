#!/usr/bin/env python3
# Copyright (c) 2026 Huawei Device Co., Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Render the final page set of a lite JS suite into a staged source tree.

The spec lists the routes to compile, one per line. Pages outside the
spec, their report items (any declared key name quoted in the page's own
code) and route references are removed.
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

_ROUTE_RE = re.compile(r"pages/[A-Za-z0-9_./-]+")
_PAGE_EXTS = (".hml", ".js", ".css")


def _delete_page_files(staged, route):
    for ext in _PAGE_EXTS:
        sibling = staged / (route + ext)
        if sibling.exists():
            sibling.unlink()


def _wipe_leftover_files(directory):
    for leftover in directory.iterdir():
        if leftover.is_file():
            leftover.unlink()


def _remove_empty_dirs(staged):
    for path in sorted(staged.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()


def collect_excluded(staged, final):
    final_set = set(final)
    excluded = []
    page_dirs = set()
    for path in sorted(staged.rglob("*.hml")):
        route = str(path.relative_to(staged))[: -len(".hml")]
        if route in final_set:
            continue
        excluded.append(route)
        page_dirs.add(path.parent)
        _delete_page_files(staged, route)
    for directory in page_dirs:
        if not any(directory.glob("*.hml")):
            _wipe_leftover_files(directory)
    _remove_empty_dirs(staged)
    return excluded


def declared_report_keys(app_path):
    return set(
        re.findall(
            r"^\s*'([A-Za-z0-9_]+)'\s*:\s*\{",
            app_path.read_text(encoding="utf-8"),
            re.M,
        )
    )


def _tier1_owners(src):
    owners = {}
    for path in src.rglob("*"):
        if path.suffix not in (".js", ".hml"):
            continue
        rel = str(path.relative_to(src))
        if rel == "app.js":
            continue
        for groups in re.findall(
            r"testItems\['([A-Za-z0-9_]+)'\]|testItems\.([A-Za-z0-9_]+)",
            path.read_text(encoding="utf-8"),
        ):
            key = groups[0] or groups[1]
            owners.setdefault(key, set()).add(rel)
    return owners


def _page_string_keys(path, declared, tier1):
    tokens = re.findall(
        r"['\"]([A-Za-z0-9_]+)['\"]", path.read_text(encoding="utf-8")
    )
    return {
        token
        for token in tokens
        if token in declared and token not in tier1
    }


def _existing_page_files(src, route):
    for ext in (".js", ".hml"):
        path = src / (route + ext)
        if path.exists():
            yield path


def collect_stripped_keys(src, excluded, declared):
    tier1 = _tier1_owners(src)
    excluded_files = {r + e for r in excluded for e in (".js", ".hml")}
    stripped = {
        key
        for key, owners in tier1.items()
        if owners and owners <= excluded_files
    }
    for route in excluded:
        for path in _existing_page_files(src, route):
            stripped |= _page_string_keys(path, declared, tier1)
    return stripped


def _matching_item_key(line, keys):
    for key in keys:
        if re.match(r"\s*'%s'\s*:" % re.escape(key), line):
            return key
    return None


def _skip_item_body(lines, index):
    depth = lines[index].count("{") - lines[index].count("}")
    index += 1
    while depth > 0 and index < len(lines):
        depth += lines[index].count("{") - lines[index].count("}")
        index += 1
    return index


def strip_report_items(staged, keys):
    if not keys:
        return
    app_path = staged / "app.js"
    lines = app_path.read_text(encoding="utf-8").splitlines(keepends=True)
    kept = []
    stripped = set()
    i = 0
    while i < len(lines):
        found = _matching_item_key(lines[i], keys)
        if found is not None:
            stripped.add(found)
            i = _skip_item_body(lines, i)
            continue
        kept.append(lines[i])
        i += 1
    missing = keys - stripped
    if missing:
        raise ValueError(
            "app.js has no report items for page keys: %s"
            % ",".join(sorted(missing))
        )
    app_path.write_text("".join(kept), encoding="utf-8")


def _check_file_keys(path, keys):
    text = path.read_text(encoding="utf-8")
    for key in keys:
        if re.search(r"['\"]%s['\"]" % re.escape(key), text):
            raise ValueError(
                "stripped report item %s is still referenced in %s"
                % (key, path)
            )


def check_stripped_keys(staged, keys):
    for path in sorted(staged.rglob("*")):
        if path.suffix in (".js", ".hml"):
            _check_file_keys(path, keys)


def route_key_map(staged):
    index_js = staged / "pages/index/index.js"
    if not index_js.exists():
        return {}
    return dict(
        re.findall(
            r"'([^']+)'\s*:\s*'(pages/[A-Za-z0-9_./-]+)'",
            index_js.read_text(encoding="utf-8"),
        )
    )


def _button_block_range(lines, index):
    start = index
    while start >= 0:
        stripped = lines[start].strip()
        if stripped.startswith("<list-item"):
            break
        if stripped == "</list-item>":
            return None
        start -= 1
    end = index
    while end < len(lines) and lines[end].strip() != "</list-item>":
        end += 1
    if start < 0 or end >= len(lines):
        return None
    return (start, end)


def _drop_buttons(path, keys):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    drop = set()
    for i, line in enumerate(lines):
        hit = re.search(r"navigateTo\('([^']+)'\)", line)
        if hit is None or hit.group(1) not in keys:
            continue
        block = _button_block_range(lines, i)
        if block is None:
            raise ValueError(
                "%s: button for '%s' is not wrapped in a list-item block"
                % (path, hit.group(1))
            )
        drop.update(range(block[0], block[1] + 1))
    if drop:
        path.write_text(
            "".join(l for i, l in enumerate(lines) if i not in drop),
            encoding="utf-8",
        )


def remove_home_buttons(staged, excluded):
    keys = {k for k, r in route_key_map(staged).items() if r in excluded}
    for path in sorted(staged.rglob("*.hml")):
        _drop_buttons(path, keys)
    return keys


def write_json(path, data):
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def process_text(path, excluded):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    kept = [
        line
        for line in lines
        if not any("'%s'" % route in line for route in excluded)
    ]
    path.write_text("".join(kept), encoding="utf-8")


def _check_file_routes(path, final_set):
    text = path.read_text(encoding="utf-8")
    for route in _ROUTE_RE.findall(text):
        if route not in final_set:
            raise ValueError(
                "%s references route %s outside the final page set"
                % (path, route)
            )


def check_final_routes(staged, final):
    final_set = set(final)
    for path in sorted(staged.rglob("*")):
        if path.suffix in (".js", ".hml", ".json"):
            _check_file_routes(path, final_set)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src-root", required=True)
    parser.add_argument("--staged-dir", required=True)
    parser.add_argument("--spec", required=True)
    parser.add_argument("--config-src", required=True)
    parser.add_argument("--config-out", required=True)
    args = parser.parse_args()

    src = Path(args.src_root)
    staged = Path(args.staged_dir)
    final = [
        line.strip()
        for line in Path(args.spec).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if not final:
        raise ValueError("spec contains no pages")
    if len(set(final)) != len(final):
        raise ValueError("spec contains duplicate routes")

    if staged.exists():
        shutil.rmtree(staged)
    shutil.copytree(src, staged)

    excluded = collect_excluded(staged, final)
    declared = declared_report_keys(src / "app.js")
    stripped_keys = collect_stripped_keys(src, excluded, declared)

    manifest_path = staged / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["pages"] = final
    write_json(manifest_path, manifest)

    config = json.loads(Path(args.config_src).read_text(encoding="utf-8"))
    for module in config["module"]["js"]:
        module["pages"] = final
    config_out = Path(args.config_out)
    config_out.parent.mkdir(parents=True, exist_ok=True)
    write_json(config_out, config)

    strip_report_items(staged, stripped_keys)
    remove_home_buttons(staged, excluded)
    for path in sorted(staged.rglob("*")):
        if path.suffix in (".js", ".hml"):
            process_text(path, excluded)
    check_stripped_keys(staged, stripped_keys)
    check_final_routes(staged, final)

    print("[js-suite] final pages: %d" % len(final))
    print(
        "[js-suite] excluded pages: %s"
        % (",".join(excluded) if excluded else "none")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
