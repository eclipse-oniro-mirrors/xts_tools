#!/usr/bin/env python3
"""Submit GitCode PR review comments as diff_comment (line-level) and/or pr_comment (summary).

Usage:
    python submit_review.py --pr <URL> --token <TOKEN> --comments comments.json
    python submit_review.py --pr <URL> --token <TOKEN> --comments comments.json --summary summary.md
    python submit_review.py --pr <URL> --token <TOKEN> --comments comments.json --dry-run

comments.json format (standard):
[
  {
    "path": "path/to/file.ext",
    "position": 100,
    "body": "**R201 (Critical)** issue description\\n\\n```\\ncode snippet\\n```\\n\\n修复建议: ...",
    "severity": "Critical"
  },
  ...
]

Also accepts XTS scanner format (auto-mapped: file->path, line->position, snippet+suggestion->body):
[
  {
    "file": "path/to/file.ext",
    "line": 100,
    "rule": "R201",
    "type": "issue description",
    "severity": "Critical",
    "snippet": "code snippet",
    "suggestion": "fix suggestion"
  },
  ...
]

If GITCODE_TOKEN env var is set, --token can be omitted.
Use --dry-run to preview, --verify to check comment types, --delete to remove comments.
"""

import argparse
import json
import os
import re
import sys

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def parse_pr_url(pr_url):
    match = re.search(r"gitcode\.com/([^/]+)/([^/]+)/pull/(\d+)", pr_url)
    if not match:
        raise ValueError(f"Invalid GitCode PR URL: {pr_url}")
    return match.group(1), match.group(2), match.group(3)


def resolve_token(token=None):
    if token:
        return token
    env_token = os.environ.get('GITCODE_TOKEN', '')
    if env_token:
        return env_token
    return None


def fetch_pr_files(base_url, headers, pr_id):
    """Fetch PR changed files with diffs."""
    url = f"{base_url}/pulls/{pr_id}/files"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


def fetch_existing_comments(base_url, headers, pr_id):
    """Fetch all existing PR comments."""
    url = f"{base_url}/pulls/{pr_id}/comments"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


def delete_comment(base_url, headers, comment_id):
    """Delete a PR comment."""
    url = f"{base_url}/comments/{comment_id}"
    resp = requests.delete(url, headers=headers, timeout=30)
    return resp.status_code in (200, 204)


def submit_diff_comment(base_url, headers, pr_id, path, position, body):
    """Submit a diff_comment (line-level review comment).

    Key: use 'position' + 'position_type: text', NOT 'line'.
    Using 'line' silently creates a pr_comment instead of diff_comment.
    """
    url = f"{base_url}/pulls/{pr_id}/comments"
    data = {
        "body": body,
        "path": path,
        "position": position,
        "position_type": "text",
    }
    resp = requests.post(url, headers=headers, json=data, timeout=30)
    return resp.status_code in (200, 201), resp


def submit_pr_comment(base_url, headers, pr_id, body):
    """Submit a pr_comment (general PR comment / summary)."""
    url = f"{base_url}/pulls/{pr_id}/comments"
    data = {"body": body}
    resp = requests.post(url, headers=headers, json=data, timeout=30)
    return resp.status_code in (200, 201), resp


def verify_comments(base_url, headers, pr_id, submitted_ids=None):
    """Fetch comments and report types. Optionally filter by submitted IDs."""
    comments = fetch_existing_comments(base_url, headers, pr_id)
    results = []
    for c in comments:
        cid = c.get('id')
        ctype = c.get('comment_type', 'unknown')
        resolved = c.get('resolved')
        diff_pos = c.get('diff_position', {})
        line = diff_pos.get('end_new_line', '-') if diff_pos else '-'
        results.append({
            'id': cid,
            'type': ctype,
            'resolved': resolved,
            'line': line,
            'body_preview': c.get('body', '')[:60],
        })
    return results


def main():
    parser = argparse.ArgumentParser(description='Submit GitCode PR review comments')
    parser.add_argument('--pr', required=True, help='GitCode PR URL')
    parser.add_argument('--token', default=None, help='GitCode PAT (or set GITCODE_TOKEN env)')
    parser.add_argument('--comments', required=True, help='JSON file with review comments')
    parser.add_argument('--summary', default=None, help='Markdown file with summary comment')
    parser.add_argument('--dry-run', action='store_true', help='Preview without submitting')
    parser.add_argument('--verify', action='store_true', help='Verify submitted comments after')
    parser.add_argument('--delete', default=None, help='Comma-separated comment IDs to delete')
    args = parser.parse_args()

    if not HAS_REQUESTS:
        print("Error: 'requests' package not installed. Run: pip install requests", file=sys.stderr)
        sys.exit(1)

    token = resolve_token(args.token)
    if not token:
        print("Error: No token. Set GITCODE_TOKEN env var or use --token", file=sys.stderr)
        sys.exit(1)

    owner, repo, pr_id = parse_pr_url(args.pr)
    base_url = f"https://api.gitcode.com/api/v5/repos/{owner}/{repo}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    print(f"[PR Review] {owner}/{repo}#{pr_id}", flush=True)

    # Delete comments if requested
    if args.delete:
        ids = [x.strip() for x in args.delete.split(',') if x.strip()]
        print(f"\n[Delete] Deleting {len(ids)} comments...", flush=True)
        for cid in ids:
            ok = delete_comment(base_url, headers, cid)
            print(f"  Delete {cid}: {'OK' if ok else 'FAIL'}", flush=True)

    # Load comments - normalize field names (path/file, position/line, body/snippet+suggestion)
    with open(args.comments, 'r', encoding='utf-8') as f:
        raw_comments = json.load(f)

    comments = []
    for c in raw_comments:
        path = c.get('path') or c.get('file', '')
        position = c.get('position') or c.get('line', 0)
        body = c.get('body', '')
        if not body:
            # Build body from snippet + suggestion (XTS scanner format)
            parts = []
            rule = c.get('rule', '')
            issue_type = c.get('type', '')
            severity = c.get('severity', '')
            if rule:
                parts.append(f"**{rule} ({severity})** {issue_type}")
            elif issue_type:
                parts.append(f"**{issue_type}**")
            snippet = c.get('snippet', '')
            if snippet:
                parts.append(f"```\n{snippet}\n```")
            suggestion = c.get('suggestion', '')
            if suggestion:
                parts.append(f"修复建议: {suggestion}")
            body = '\n\n'.join(parts)
        comments.append({
            'path': path,
            'position': position,
            'body': body,
            'severity': c.get('severity', '?'),
        })

    print(f"\n[Submit] {len(comments)} diff_comment (line-level) comments", flush=True)

    if args.dry_run:
        for c in comments:
            print(f"  [dry-run] {c['path']}:{c['position']} - {c['severity']} - {c['body'][:50]}...", flush=True)
        if args.summary:
            with open(args.summary, 'r', encoding='utf-8') as f:
                summary_body = f.read()
            print(f"  [dry-run] Summary: {len(summary_body)} chars", flush=True)
        print("\n[dry-run] No comments submitted.", flush=True)
        return

    # Submit diff_comment for each issue
    success_count = 0
    fail_count = 0
    for c in comments:
        ok, resp = submit_diff_comment(
            base_url, headers, pr_id,
            c['path'], c['position'], c['body']
        )
        if ok:
            success_count += 1
            print(f"  [OK] {c['path']}:{c['position']} ({c['severity']})", flush=True)
        else:
            fail_count += 1
            print(f"  [FAIL] {c['path']}:{c['position']} - HTTP {resp.status_code}: {resp.text[:200]}", flush=True)

    # Submit summary if provided
    if args.summary:
        with open(args.summary, 'r', encoding='utf-8') as f:
            summary_body = f.read()
        print(f"\n[Submit] Summary comment ({len(summary_body)} chars)...", flush=True)
        ok, resp = submit_pr_comment(base_url, headers, pr_id, summary_body)
        if ok:
            success_count += 1
            print(f"  [OK] Summary submitted", flush=True)
        else:
            fail_count += 1
            print(f"  [FAIL] Summary - HTTP {resp.status_code}: {resp.text[:200]}", flush=True)

    print(f"\n[Result] Success: {success_count}, Failed: {fail_count}", flush=True)

    # Verify if requested
    if args.verify:
        print(f"\n[Verify] Fetching all PR comments...", flush=True)
        all_comments = verify_comments(base_url, headers, pr_id)
        for c in all_comments:
            line_info = f"line={c['line']}" if c['type'] == 'diff_comment' else ''
            resolved_info = f" resolved={c['resolved']}" if c['type'] == 'diff_comment' else ''
            print(f"  ID={c['id']} type={c['type']}{resolved_info} {line_info} body={c['body_preview']}...", flush=True)

    if fail_count > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
