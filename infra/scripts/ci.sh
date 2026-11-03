#!/usr/bin/env bash
set -euo pipefail
ROOT="${CI_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"
cd "$ROOT"
"$ROOT/infra/scripts/ci/validate-repo.sh" --root "$ROOT"
"$ROOT/infra/scripts/ci/check-size.sh" --root "$ROOT"
"$ROOT/infra/scripts/check-layout.sh" --root "$ROOT"
cargo check --all-targets
python3 -m unittest discover -s src/bots/solver -p "test_*.py"
