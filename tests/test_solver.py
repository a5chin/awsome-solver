import sys  # noqa:INP001
from pathlib import Path

import pytest

current_dir = Path(__file__).resolve().parent
sys.path.append(current_dir.parent.as_posix())

from solver import Solver  # noqa: E402


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        (
            [
                [3, 4, 2, 0, 0, 0, 0, 8, 1],
                [0, 0, 0, 0, 8, 2, 0, 0, 4],
                [7, 0, 0, 4, 0, 6, 3, 9, 0],
                [9, 7, 0, 0, 6, 0, 0, 0, 8],
                [0, 0, 4, 0, 0, 0, 2, 0, 5],
                [0, 3, 0, 5, 0, 8, 9, 6, 0],
                [0, 1, 9, 0, 5, 0, 0, 2, 0],
                [0, 0, 0, 9, 0, 1, 8, 0, 6],
                [5, 6, 0, 0, 0, 4, 7, 1, 0],
            ],
            [
                [3, 4, 2, 7, 9, 5, 6, 8, 1],
                [1, 9, 6, 3, 8, 2, 5, 7, 4],
                [7, 5, 8, 4, 1, 6, 3, 9, 2],
                [9, 7, 5, 2, 6, 3, 1, 4, 8],
                [6, 8, 4, 1, 7, 9, 2, 3, 5],
                [2, 3, 1, 5, 4, 8, 9, 6, 7],
                [8, 1, 9, 6, 5, 7, 4, 2, 3],
                [4, 2, 7, 9, 3, 1, 8, 5, 6],
                [5, 6, 3, 8, 2, 4, 7, 1, 9],
            ],
        ),
        (
            [
                [0, 9, 0, 6, 0, 1, 0, 2, 0],
                [8, 0, 0, 0, 0, 0, 0, 0, 3],
                [0, 0, 0, 8, 4, 2, 5, 0, 0],
                [7, 0, 6, 0, 0, 0, 9, 0, 8],
                [0, 0, 1, 0, 5, 0, 7, 0, 0],
                [3, 0, 5, 0, 0, 0, 4, 0, 6],
                [0, 0, 9, 5, 1, 8, 6, 0, 0],
                [4, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 2, 0, 4, 0, 8, 0],
            ],
            [
                [5, 9, 4, 6, 3, 1, 8, 2, 7],
                [8, 6, 2, 9, 7, 5, 1, 4, 3],
                [1, 7, 3, 8, 4, 2, 5, 6, 9],
                [7, 4, 6, 1, 2, 3, 9, 5, 8],
                [9, 8, 1, 4, 5, 6, 7, 3, 2],
                [3, 2, 5, 7, 8, 9, 4, 1, 6],
                [2, 3, 9, 5, 1, 8, 6, 7, 4],
                [4, 5, 8, 3, 6, 7, 2, 9, 1],
                [6, 1, 7, 2, 9, 4, 3, 8, 5],
            ],
        ),
    ],
)
def test__solver(example: list[list[int]], expected: list[list[int]]) -> None:
    """Tests of Number Place Solver.

    Args:
    ----
        example (list[list[int]]): The problem of Number Place.
        expected (list[list[int]]): The solved Number Place.

    """
    solver = Solver()
    result = solver.solve(example)

    assert result == expected  # noqa: S101
