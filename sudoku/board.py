class Board:
    """A class to represent a Number Place board.

    Attributes
    ----------
        BLOCK_SIZE (int): The size of block. Defaults to 3.

    """

    BLOCK_SIZE = 3
    BOARD_SIZE = BLOCK_SIZE * BLOCK_SIZE

    def __init__(self: "Board", board: list[list[int]]) -> None:
        """Construct all the necessary attributes for the Board object.

        Args:
        ----
            board (list[list[int]]): The 9x9 cells representing the Number Place board.
            index (int): The current index for iteration.

        """
        self.board = board
        self.index = 0

    def tolist(self: "Board") -> list[list[int]]:
        """Return the Sudoku board as a 2D list of integers.

        Returns
        -------
            list[list[int]]: The Number Place board as a 2D list of integers.

        """
        return self.board

    def __getitem__(self: "Board", index: int) -> list[int]:
        """Allow for subscriptable access to the board elements.

        Args:
        ----
            index (int): The row index of the board.

        Returns:
        -------
            list[int]: The specified row of the board.

        """
        return self.board[index]

    def __iter__(self: "Board") -> "Board":
        """Reset the iteration index and returns the iterator object."""
        self.index = 0

        return self

    def __next__(self: "Board") -> list[int]:
        """Return the next element in the board.

        Raises
        ------
            StopIteration: If the end of the board is reached.

        Returns
        -------
            int: The next element in the board.

        """
        if self.index >= Board.BOARD_SIZE:
            raise StopIteration

        it = self.board[self.index]
        self.index += 1

        return it

    def __eq__(self: "Board", other: "Board") -> bool:
        """Check if two Board objects are equal.

        Args:
        ----
            other (Board): The other Board object to compare with.

        Returns:
        -------
            bool: True if the two boards are equal, False otherwise.

        """
        if not isinstance(other, Board):
            return False

        return self.board == other.board

    def __str__(self: "Board") -> str:
        """Return a string representation of the board formatted for easy reading.

        The board is displayed in a grid format with vertical and horizontal separators
        to distinguish the 3x3 blocks, as shown below:

        8 1 2 | 7 5 3 | 6 4 9
        9 4 3 | 6 8 2 | 1 7 5
        6 7 5 | 4 9 1 | 2 8 3
        - - - + - - - + - - -
        1 5 4 | 2 3 7 | 8 9 6
        3 6 9 | 8 4 5 | 7 2 1
        2 8 7 | 1 6 9 | 5 3 4
        - - - + - - - + - - -
        5 2 1 | 9 7 4 | 3 6 8
        4 3 8 | 5 2 6 | 9 1 7
        7 9 6 | 3 1 8 | 4 5 2

        Returns
        -------
            str: A string representation of the Number Place board.

        """
        board_str = ""

        for i, row in enumerate(self.board):
            row_str = " | ".join(
                " ".join(str(cell) for cell in row[start : start + Board.BLOCK_SIZE])
                for start in range(0, len(row), Board.BLOCK_SIZE)
            )
            board_str += row_str + "\n"

            if (i + 1) % Board.BLOCK_SIZE == 0 and (i + 1) < len(self.board):
                board_str += "- - - + - - - + - - -\n"

        return board_str.strip()
