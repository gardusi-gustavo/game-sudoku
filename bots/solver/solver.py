"""Deterministic sudoku bot: validate a grid and return a solved grid."""
from __future__ import annotations

import json
import sys
from collections.abc import Iterable

SIZE = 9
EMPTY = 0


def _validate(grid: list[list[int]]) -> None:
    if len(grid) != SIZE or any(len(row) != SIZE for row in grid):
        raise ValueError("grid must be 9x9")
    for row in grid:
        for value in row:
            if not isinstance(value, int) or not 0 <= value <= 9:
                raise ValueError("cells must be integers from 0 to 9")


def _candidates(grid: list[list[int]], row: int, col: int) -> set[int]:
    used = set(grid[row]) | {grid[r][col] for r in range(SIZE)}
    box_row, box_col = row // 3 * 3, col // 3 * 3
    used |= {
        grid[r][c]
        for r in range(box_row, box_row + 3)
        for c in range(box_col, box_col + 3)
    }
    return set(range(1, 10)) - used


def solve(grid: Iterable[Iterable[int]]) -> list[list[int]]:
    """Return a solved copy of the grid, or raise ValueError if unsolvable."""
    board = [list(row) for row in grid]
    _validate(board)

    def backtrack() -> bool:
        best: tuple[int, int, set[int]] | None = None
        for row in range(SIZE):
            for col in range(SIZE):
                if board[row][col] != EMPTY:
                    continue
                choices = _candidates(board, row, col)
                if not choices:
                    return False
                if best is None or len(choices) < len(best[2]):
                    best = (row, col, choices)
                    if len(choices) == 1:
                        break
            if best and len(best[2]) == 1:
                break
        if best is None:
            return True
        row, col, choices = best
        for value in sorted(choices):
            board[row][col] = value
            if backtrack():
                return True
        board[row][col] = EMPTY
        return False

    if not backtrack():
        raise ValueError("grid has no solution")
    return board


def _read_grid() -> list[list[int]]:
    if len(sys.argv) > 1:
        payload = json.loads(open(sys.argv[1], encoding="utf-8").read())
    else:
        payload = json.load(sys.stdin)
    grid = payload["grid"] if isinstance(payload, dict) else payload
    return grid


def main() -> None:
    try:
        solution = solve(_read_grid())
    except (ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}))
        raise SystemExit(1) from None
    print(json.dumps({"solution": solution}))


if __name__ == "__main__":
    main()
