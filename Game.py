#!/usr/bin/python3

"""
Main Ocean class for representing and getting information from the grid.
"""

import Util

class Ocean:
    def __init__(self, grid: list[list[bool]]):
        """
        Create an ocean with the given 2D Boolean grid of whether a ship is in
        each position. An AssertionError will be thrown if it is invalid.
        """
        self.grid = grid
        self.height = len(grid)
        assert self.height >= 1, "Grid must be at least 1x1"
        self.width = len(grid[0])
        assert self.width >= 1, "Grid must be at least 1x1"
        for row in grid:
            assert len(row) == self.width, "All rows in grid must have same width"

        # TODO: Calculate fleet and verify valid
        self.fleet = dict()
        for row_index, row in enumerate(grid):
            for col_index, cell in enumerate(row):
                if cell:
                    pass

    def getWidth(self) -> int:
        """
        Get the width of the ocean grid (length of outer list).
        """
        return self.width

    def getHeight(self) -> int:
        """
        Get the height of the ocean grid (length of inner lists).
        """
        return self.height

    def getFleet(self) -> dict[int, int]:
        """
        Return a dictionary from size of ship to number of those ships in the
        ocean.
        """
        return self.fleet

    def getRowNums(self) -> list[int]:
        """
        Return a list of length equal to the height with the number of ocean
        cells in that row containing (part of a) ship.
        """
        return [sum(int(cell) for cell in row) for row in self.grid]

    def getColNums(self) -> list[int]:
        """
        Return a list of length equal to the width with the number of ocean
        cells in that column containing (part of a) ship.
        """
        return [sum(int(row[col_index]) for row in self.grid) for col_index in range(self.width)]

    def __str__(self):
        """
        Return a string representation of the grid 
        """

        max_len_row_num = max(len(str(num)) for num in self.getRowNums())
        max_len_col_num = max(len(str(num)) for num in self.getColNums())

        out = " " * (max_len_row_num + 2) \
            + " ".join(map(Util.padCentreFunc(max_len_col_num), self.getColNums())) \
            + "\n" + " " * (max_len_row_num + 1) \
            + "+" + "-" * ((max_len_col_num + 1) * self.getWidth() - 1)

        for row, row_num in zip(self.grid, self.getRowNums()):
            out += "\n" + Util.padCentre(row_num, max_len_row_num) + " |" \
                + " ".join(Util.padCentre("x" if cell else " ", max_len_col_num) for cell in row)

        return out

    def __eq__(self, other):
        """
        Return whether 'other' represents the same grid as this object.
        """
        if isinstance(other, Ocean):
            other = other.grid
        return other == self.grid
