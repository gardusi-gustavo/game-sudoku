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
## Local tasks

- The backlog is `docs/issues/`, one JSON file per task.
- Append tasks; do not rewrite task history.
- Rank: `3.x` bugs, `2.x` documentation/chores, `1.x` features/refactors.
  Higher fraction = more important.
- Filename: `<rank>-<slug>.json`; no trailing zero; one to six fractional digits.
- The file is the task. There is no author, source, platform, or status field.
- Pick the highest-ranked task.
- One work PR per repository.
- Open one native issue for the work item when the pull request starts.
- The PR references the task and the issue:
  `Task: docs/issues/<file>.json` and `Closes #N`.
- Merge deletes the task file and closes the issue. Git history keeps the record.
- On a failed PR, append an attempt to the task file, close the PR, and keep the file.
- Native issues created by the owner or external contributors remain native.
<!-- end local-issues -->

## Shared rules

- Follow the repository layout and build instructions in `README.md`.
- Use Git tags; do not publish release artifacts without an issue.
- Do not add editor or devcontainer configuration.

## Repository-specific rules

Add repository-specific behavior, constraints, and commands here.
