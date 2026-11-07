# AGENTS.md

## Start here

- Read `README.md`.
- Read `docs/README.md`.
- Search open Gitea issues before starting.

<!-- begin issue-workflow -->
## Issue tracker

The backlog is `docs/issues/`; native issues only track an item that has an open
pull request.

- Pick the highest-ranked task in `docs/issues/`.
- Open one native issue for that work item when the pull request starts.
- The pull request references the issue (`Part of #N` or `Closes #N`).
- Merging the pull request deletes the task file and closes the issue.
- A failed attempt appends to the task file and keeps it.
- Native issues created by the owner or external contributors stay native.
- One open pull request per repository and one issue per work item.
- Ranked native titles remain `3.x` bug, `2.x` documentation, `1.x` feature.
- Prefer the `gitea-api` helper for Gitea actions.
- When a pull request deletes files, add a `## Deletions` section.
- The bot may comment and open pull requests that reference an open issue; it
  does not create, edit, close, or relabel issues.
<!-- end issue-workflow -->

<!-- begin local-issues -->
## Local work records

- Agent work is tracked in `docs/issues/`, not in new native issues.
- Use `3.x` for bugs, `2.x` for documentation and chores, and `1.x` for
  features and code refactors. Higher fraction = more important.
- Filename: `<rank>-<slug>.json`; no trailing zero; one to six fractional digits.
- Exactly zero or one file may have `status: active`.
- Only the active file gets a native issue. Record `platform_issue_id` and
  `platform_issue_url` in it.
- A PR references the active file and closes the native issue:
  `Local-Issue: docs/issues/<file>.json` and `Closes #N`.
- On a failed PR, append an attempt locally, post the same summary on the native
  issue, close the PR, and keep the local file.
- On merge, delete the local file; the native issue closes through `Closes #N`.
- Native issues get one core label: `bug`, `documentation`, or `enhancement`.
  Keep security and area classification in local `tags`.
- Do not create extra native issues for agent work.
<!-- end local-issues -->

## Shared rules

- Follow the repository layout and build instructions in `README.md`.
- Use Git tags; do not publish release artifacts without an issue.
- Do not add editor or devcontainer configuration.

## Repository-specific rules

Add repository-specific behavior, constraints, and commands here.
