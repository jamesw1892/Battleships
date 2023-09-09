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

        # Create a deep copy of grid to calculate fleet and check valid
        self.fleet = dict()
        grid_cp = []
        for row in grid:
            grid_cp.append(row.copy())

        # Go through cells top to bottom and within that, left to right.
        # If find a ship: (1) extend it as far as possible right or down (as
        # can't extend up or left), (2) unset those cells in the copy so we
        # don't see them in subsequent iterations, (3) check surrounding cells
        # aren't ships as would be invalid, and (4) add to fleet.
        # When checking surrounding cells, we only need to check those down and
        # right (as would have seen in subsequent iteration) and we don't need
        # to check those at the far end or we would have extended it further.
        for r in range(self.height):
            for c in range(self.width):
                if grid_cp[r][c]:
                    grid_cp[r][c] = False

                    # If extends right
                    if c + 1 < self.width and grid_cp[r][c + 1]:
                        size = 2
                        grid_cp[r][c + 1] = False

                        # Extend all the way, unsetting as go
                        while c + size < self.width and grid_cp[r][c + size]:
                            grid_cp[r][c + size] = False
                            size += 1

                        # Check surrounding cells aren't ships
                        if r + 1 < self.height:
                            for c2 in range(max(c - 1, 0), min(c + size + 1, self.width - 1)):
                                assert not grid_cp[r + 1][c2], f"Cross of ships around cell ({c2}, {r})!"

                    # If extends down
                    elif r + 1 < self.height and grid_cp[r + 1][c]:
                        size = 2
                        grid_cp[r + 1][c] = False

                        # Extend all the way, unsetting as go
                        while r + size < self.height and grid_cp[r + size][c]:
                            grid_cp[r + size][c] = False
                            size += 1

                        # Check surrounding cells aren't ships
                        if c > 0:
                            for r2 in range(r + 1, min(r + size + 1, self.height - 1)):
                                assert not grid_cp[r2][c - 1], f"Cross of ships around cell ({c}, {r2})"
                        if c + 1 < self.width:
                            for r2 in range(r, min(r + size + 1, self.height - 1)):
                                assert not grid_cp[r2][c + 1], f"Cross of ships around cell ({c}, {r2})"

                    # If neither then is a size 1 ship
                    else:
                        size = 1

                    # Add to fleet
                    if size in self.fleet:
                        self.fleet[size] += 1
                    else:
                        self.fleet[size] = 1

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
