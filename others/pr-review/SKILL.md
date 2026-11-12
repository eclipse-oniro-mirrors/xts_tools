---
name: pr-review
description: >
  Review GitCode PRs (Pull Requests) and submit diff-level review comments on specific code lines.
  Use this skill when the user asks to review/inspect a GitCode PR, add review comments on file changes,
  or check code quality of a PR. Triggers on phrases like "检视PR", "review PR", "代码评审",
  "文件变动增加评论", "review this pull request", "检查PR有没有问题", "添加评审意见".
  Supports any GitCode repository PR. Works with ohos-test-xts-code-quality skill for XTS-specific rules.
---

# GitCode PR Review

Review a GitCode Pull Request, identify code quality issues, and submit **diff-level** review comments
(`diff_comment`) that are attached to specific code lines — clickable, visible in the Files Changed
review panel, and resolvable/unresolvable.

## Quick Start Checklist

Before first use, complete these one-time steps:

- [ ] **Create GitCode PAT**: Visit https://gitcode.com/setting/token-classic → Create token with `api` scope
- [ ] **Set token env var**: `[Environment]::SetEnvironmentVariable("GITCODE_TOKEN", "<token>", "User")` (persistent, PowerShell)
- [ ] **Verify Python**: `python --version` (need 3.x)
- [ ] **Verify requests**: `python -c "import requests"` → if missing: `pip install requests`
- [ ] **Verify token**: `python -c "import requests; print(requests.get('https://api.gitcode.com/api/v5/user', headers={'Authorization':'Bearer <token>'}).status_code)"` → expect 200

Then just say: **"检视 PR https://gitcode.com/{owner}/{repo}/pull/{number}"**

## Prerequisites

Before using this skill, complete the following setup. This is a one-time configuration.

### 1. GitCode Personal Access Token (PAT)

The skill needs a PAT to call the GitCode API for fetching PR diffs and submitting review comments.

**Step-by-step to create a token:**

1. Log in to [GitCode](https://gitcode.com)
2. Visit **https://gitcode.com/setting/token-classic** (or click avatar → Settings → Personal Access Tokens)
3. Click **Create Token** / **新建令牌**
4. Fill in:
   - **Name**: e.g. `pr-review` (any descriptive name)
   - **Scopes**: select **`api`** (required — grants read/write access to PR comments, files, etc.)
   - **Expiration**: set as needed (recommend 90 days+)
5. Click **Submit** / **提交**
6. **Copy the token immediately** — it will not be shown again. Format: alphanumeric string like `3yxSLnfax3qSyBZ_UbGhzcD9`

> If the token URL above doesn't work, try: avatar → 设置 → 个人访问令牌, or `https://gitcode.com/-/settings/tokens`

**Configure the token (choose one method):**

| Method | Command | Persistence |
|--------|---------|-------------|
| **Env var (PowerShell)** | `$env:GITCODE_TOKEN="<your-token>"` | Current session only |
| **Env var (persistent)** | `[Environment]::SetEnvironmentVariable("GITCODE_TOKEN", "<your-token>", "User")` | Survives restart (recommended) |
| **Env var (Linux/Mac)** | `export GITCODE_TOKEN="<your-token>"` (add to `~/.bashrc`) | Session or permanent |
| **CLI arg** | `--token "<your-token>"` on each script call | Per-invocation |
| **oh-gc CLI** | `npm install -g @oh-gc-cli && oh-gc auth:login` | Managed by oh-gc |

**Verify the token works:**

```bash
python -c "import requests; r=requests.get('https://api.gitcode.com/api/v5/user', headers={'Authorization':'Bearer <your-token>'}); print(r.status_code, r.json().get('login','FAIL'))"
```

Expected output: `200 your_username`

### 2. Python Environment

Requires Python 3.x with the `requests` library.

```bash
# Check Python
python --version   # need 3.x

# Check requests
python -c "import requests; print('requests', requests.__version__)"

# Install if missing
pip install requests
```

### 3. Token Scope Requirements

| API Operation | Required Scope |
|---------------|----------------|
| Read PR files / diffs | `api` (or `read_repository`) |
| Submit PR comments | `api` |
| Delete PR comments | `api` |
| Update resolved status | `api` |

The `api` scope covers all operations. No additional scopes needed.

## Workflow

### Step 1: Fetch PR file changes

Get the list of changed files and their diffs via the GitCode API:

```
GET https://api.gitcode.com/api/v5/repos/{owner}/{repo}/pulls/{pr_number}/files
Authorization: Bearer {token}
```

This returns a JSON array. Each element contains:
- `filename` — file path
- `additions` / `deletions` — line counts
- `new_file` / `deleted_file` / `renamed_file` — booleans
- `patch.diff` — unified diff text (the full patch string)

Parse the diff to extract:
- Changed file paths
- Added lines (lines starting with `+`)
- Line numbers in the new file (use the `@@ -old,count +new,count @@` hunk headers)

Alternatively, use `webfetch` on the PR diffs page `https://gitcode.com/{owner}/{repo}/pull/{pr_number}/diffs`
and delegate parsing to a subagent if the API is unavailable.

### Step 2: Analyze code quality

Review each changed file for issues. For OpenHarmony XTS test code (`.ets`/`.ts`/`.js` test files),
also load the `ohos-test-xts-code-quality` skill or run its scanner for rule-based detection.

Common review categories:

| Category | What to check |
|----------|---------------|
| Async safety | `done()` called before async callbacks resolve; `done()` without `return` after failure; multiple `done()` calls |
| Assertions | Missing `expect()` in success/failure branches; only `console.log` without verification |
| Resource leaks | `FetchResult` not closed; `PixelMap` not released; file handles not closed |
| Logic errors | Accessing potentially-undefined objects after null check without return; wrong variable references |
| Code quality | Unused imports; misleading log messages; inconsistent indentation |

For each issue, record:
- **File path** (exact path from the diff)
- **Line number** (in the new file, from the diff hunk)
- **Severity** (Critical / Warning)
- **Rule ID** (if using XTS rules, e.g. R201, R004, R204)
- **Description** + **code snippet** + **fix suggestion**

### Step 3: Submit diff-level review comments

This is the critical step. GitCode has **two types** of PR comments:

| Type | `comment_type` | API parameters | Behavior |
|------|---------------|----------------|----------|
| Regular PR comment | `pr_comment` | `body` only | Shows in PR discussion tab |
| **Diff review comment** | `diff_comment` | `body` + `path` + `position` + `position_type` | Attached to code line, clickable, resolvable |

**Always use `diff_comment` for line-level review comments.** Regular `pr_comment` comments do not
appear in the Files Changed review panel and cannot be resolved.

#### API: Create a diff_comment

```
POST https://api.gitcode.com/api/v5/repos/{owner}/{repo}/pulls/{pr_number}/comments
Authorization: Bearer {token}
Content-Type: application/json

{
  "body": "comment text (markdown supported)",
  "path": "path/to/file.ext",
  "position": 100,
  "position_type": "text"
}
```

- `position` — the **line number in the new file** (the file after changes)
- `position_type` — always `"text"` for code line comments; `"binary"` for file-level comments

#### API: Create a summary comment (pr_comment)

```
POST https://api.gitcode.com/api/v5/repos/{owner}/{repo}/pulls/{pr_number}/comments
Authorization: Bearer {token}
Content-Type: application/json

{
  "body": "## Review Summary\n\n..."
}
```

#### Using the bundled script

Instead of writing ad-hoc Python each time, use the bundled script:

```bash
python {SKILL_DIR}/scripts/submit_review.py \
  --pr "https://gitcode.com/{owner}/{repo}/pull/{number}" \
  --token "<your-token>" \
  --comments review_comments.json \
  --summary summary.md \
  [--dry-run]
```

**comments.json format** (two supported formats):

Standard format:
```json
[
  {
    "path": "path/to/file.ext",
    "position": 100,
    "body": "**R201 (Critical)** issue description\n\n```\ncode snippet\n```\n\n修复建议: ...",
    "severity": "Critical"
  }
]
```

XTS scanner format (fields auto-mapped: `file`→`path`, `line`→`position`, `snippet`+`suggestion`→`body`):
```json
[
  {
    "file": "path/to/file.ext",
    "line": 100,
    "rule": "R201",
    "type": "issue description",
    "severity": "Critical",
    "snippet": "code snippet",
    "suggestion": "fix suggestion"
  }
]
```

Options: `--dry-run` to preview, `--verify` to check submitted types, `--delete id1,id2` to remove comments.

### Step 4: Verify submitted comments

Fetch all PR comments and verify the new ones are `diff_comment` type:

```
GET https://api.gitcode.com/api/v5/repos/{owner}/{repo}/pulls/{pr_number}/comments
Authorization: Bearer {token}
```

Check that each submitted comment has:
- `"comment_type": "diff_comment"`
- `"resolved": false`
- `"diff_position.end_new_line"` matches the intended line

## Common Pitfalls

### `line` vs `position`

The GitCode API uses `position` (not `line`) for the line number parameter. Using `line` will
silently create a `pr_comment` instead of a `diff_comment`.

### File path must match exactly — always fetch from API

The `path` parameter must match the exact file path as stored in GitCode. **Never guess or
construct file paths from the diff display** — always fetch them from the API:

```
GET /repos/{owner}/{repo}/pulls/{number}/files → response[].filename
```

A common mistake is omitting intermediate directory segments. For example, a file might appear
in the diff page as `entry/src/test/Foo.test.ets` but the actual API path is
`entry/src/main/src/test/Foo.test.ets`. Using the wrong path causes HTTP 400:
`"diff failed to be generated due to invalid params under position param."`

### New files vs modified files

Both new files (entirely added) and modified files support `diff_comment` with `position` +
`position_type: "text"`. For new files, the diff hunk is `@@ -0,0 +1,N @@` and `position`
is simply the line number within the new file (starting from 1).

### Comment ID formats

The GitCode API returns two ID fields when creating a comment:
- `id` — string hash (e.g. `"dd1a3c34a3b6..."`) — **not** usable for DELETE
- `note_id` — integer (e.g. `200289106`) — **use this** for DELETE operations

When deleting comments, always use the integer `note_id`, not the string `id`.

### Line number must be in the new file

The `position` refers to the line number in the **new file** (after changes), not the old file.
Always calculate line numbers from the `+new,count` side of the diff hunk header.

### Console encoding on Windows

When printing Chinese/Unicode content to PowerShell, set `PYTHONUTF8=1` or write output to a
file with `encoding='utf-8'` to avoid `UnicodeEncodeError: 'gbk' codec can't encode...`.

### Fetching all comments requires pagination

The GET comments API returns 20 comments per page by default. For PRs with many comments,
use `?page=1&per_page=100` and iterate until a page returns fewer than `per_page` items.

### Deleting incorrect comments

If you accidentally submitted `pr_comment` instead of `diff_comment`:

```
DELETE https://api.gitcode.com/api/v5/repos/{owner}/{repo}/pulls/comments/{note_id}
Authorization: Bearer {token}
```

Then re-submit with the correct `position` + `position_type` parameters.
Use the integer `note_id` (not string `id`) in the DELETE URL.

## API Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/repos/{owner}/{repo}/pulls/{number}/files` | GET | Get changed files + diffs |
| `/repos/{owner}/{repo}/pulls/{number}/comments` | GET | List all comments |
| `/repos/{owner}/{repo}/pulls/{number}/comments` | POST | Create comment (diff or pr) |
| `/repos/{owner}/{repo}/pulls/comments/{id}` | GET | Get single comment |
| `/repos/{owner}/{repo}/pulls/comments/{id}` | DELETE | Delete a comment |
| `/repos/{owner}/{repo}/pulls/{number}/comments/{discussions_id}` | PUT | Update resolved status |

Base URL: `https://api.gitcode.com/api/v5`

## Comment Format Guidelines

### Line-level review comment

```markdown
**R201 (Critical)** 异步用例done()后未return，执行继续导致潜在崩溃

```
if (photoAsset === undefined) {
  expect(false).assertTrue()
  done();
}
if (photoAsset.uri === undefined) {  // 会抛TypeError
```

修复建议: 在done()后添加return语句提前退出。
```

### Summary comment

```markdown
## 代码质量检视报告

**PR**: {owner}/{repo}#{number}
**文件**: `changed_file.ext` (+N, -M)

### 扫描统计

| 严重级别 | 问题数量 |
|----------|----------|
| Critical | N |
| Warning | M |

### 问题清单

| # | 规则 | 严重级别 | 行号 | 问题 |
|---|------|----------|------|------|
| 1 | R201 | Critical | 100 | 问题描述 |

### 修复建议
1. ...
2. ...
```
