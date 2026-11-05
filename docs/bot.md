# Bot manifest — Sudoku

Manifest for the Sudoku-solving bot.

| Field | Value |
| --- | --- |
| Kind | bot (solver) |
| Base | deterministic solver; learned model optional |
| Method | solver baseline; learned model TBD |
| Dataset | game-specific; not committed |
| Bot | `src/bots/` in this repository |
| Weights | not committed; release artifact |
| Status | deterministic baseline bot; model pending |

## Rules

- The solver is the baseline.
- A learned model must beat the baseline on replay-scored sessions.
- Replays and seeds are recorded.
- Weights are artifacts, not source data.

## Related

- Replay-scored bot: `games/sudoku#13`
- Bot protocol: `packages/rust-game-kit#13`
- Evaluation harness: `games/launcher#25`
