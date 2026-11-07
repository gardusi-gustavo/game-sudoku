# Repository self-containment

**What this is:** the checklist for making this repository understandable,
recoverable, and copyable without Gitea.

## Source of truth

- Repository: `games/sudoku`
- Visibility: public
- Owner: `gardusi-gustavo`
- Git platform: Gitea
- Local checkout: `~/repos/games/sudoku`

## Durable data

- [x] `README.md` and `AGENTS.md`
- [x] `docs/README.md`
- [x] `docs/issues/`
- [x] decisions and operating rules in AGENTS
- [x] runbooks and contract docs
- [x] `VERSION`
- [ ] `CHANGELOG.md`
- [x] release tags
- [x] `infra/config/repo.json`
- [x] CI workflow
- [ ] tests
- [x] external service references
- [x] backup and restore notes

## External-only data

- issues and comments: Gitea owner issues
- PR discussions: Gitea
- attachments and media: external storage
- secrets: repository secret stores
- package registry artifacts: external registries
- external services: Gitea and data sources

## Migration status

- [x] Agent-created issues migrated to `docs/issues/`
- [ ] Owner-created issues classified
- [ ] Closed history exported to backup
- [x] Wiki content not applicable
- [ ] GitHub v1 issue created

## Copy test

1. Clone the repository.
2. Read the docs and understand the domain contract.
3. Find all open work in `docs/issues/`.
4. Run CI.
5. Recover external dependencies from the recorded references.
