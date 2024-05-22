import mip

from .board import Board


class Solver:
    """A class to represent a Number Place solver using linear programming.

    Attributes
    ----------
        BLOCK_SIZE (int):
            Size of each block in the Number Place cell. Defaults to 3.
        N (int):
            Size of the Number Place grid. Defaults to 9.

    Methods
    -------
        _add_constraints:
            Add all necessary constraints to the linear programming problem.
        _set_values:
            Set values from the initial cell as constraints in the problem.
        solve:
            Solve the Number Place and returns the solved cell.

    """

    BLOCK_SIZE = 3
    BOARD_SIZE = BLOCK_SIZE * BLOCK_SIZE

    def __init__(self: "Solver") -> None:
        """Construct all the necessary attributes for the Solver object."""
        self.model = mip.Model("NumberPlace", mip.MINIMIZE)
        self.cell = [
            [
                [
                    self.model.add_var(var_type=mip.BINARY)
                    for _ in range(Solver.BOARD_SIZE)
                ]
                for _ in range(Solver.BOARD_SIZE)
            ]
            for _ in range(Solver.BOARD_SIZE)
        ]

    def _add_constraints(self: "Solver") -> None:
        """Add all necessary constraints to the linear programming problem."""
        for num in range(Solver.BOARD_SIZE):
            for i in range(Solver.BOARD_SIZE):
                self.model += (
                    mip.xsum(self.cell[i][j][num] for j in range(Solver.BOARD_SIZE))
                    == 1
                )
                self.model += (
                    mip.xsum(self.cell[j][i][num] for j in range(Solver.BOARD_SIZE))
                    == 1
                )

            for block_row in range(Solver.BLOCK_SIZE):
                for block_col in range(Solver.BLOCK_SIZE):
                    self.model += (
                        mip.xsum(
                            self.cell[i][j][num]
                            for i in range(
                                Solver.BLOCK_SIZE * block_row,
                                Solver.BLOCK_SIZE * (block_row + 1),
                            )
                            for j in range(
                                Solver.BLOCK_SIZE * block_col,
                                Solver.BLOCK_SIZE * (block_col + 1),
                            )
                        )
                        == 1
                    )

        for row in range(Solver.BOARD_SIZE):
            for col in range(Solver.BOARD_SIZE):
                self.model += (
                    mip.xsum(
                        self.cell[row][col][num] for num in range(Solver.BOARD_SIZE)
                    )
                    == 1
                )

    def _set_values(
        self: "Solver", prob: list[list[int]], values: tuple = range(1, 10)
    ) -> None:
        """Set values of Number Place Problem."""
        for i in range(Solver.BOARD_SIZE):
            for j in range(Solver.BOARD_SIZE):
                if prob[i][j] in values:
                    self.model += self.cell[i][j][prob[i][j] - 1] == 1

    def solve(self: "Solver", prob: list[list[int]]) -> Board:
        """Solve the Number Place.

        Args:
        ----
            prob (list[list[int]]): The problem of Number Place.
            values (tupple): Numbers to treat as problem.

        Returns:
        -------
            Board: The solved Number Place cell if a solution exists.
                   None: If no solution exists.

        """
        self._add_constraints()
        self._set_values(prob, values=range(1, Solver.BOARD_SIZE + 1))
        self.model.optimize()

        if not self.model.num_solutions:
            return None

        result = [
            [
                next(
                    k + 1 for k in range(Solver.BOARD_SIZE) if self.cell[i][j][k].x >= 1
                )
                for j in range(Solver.BOARD_SIZE)
            ]
            for i in range(Solver.BOARD_SIZE)
        ]

        return Board(result)
