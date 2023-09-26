#!/usr/bin/python3

"""
Main Ocean class for representing and getting information from the grid.
"""

import Util
from enum import Enum

class VisibleCell(Enum):
    """
    An enum representing a visible cell in the grid that is given at the start.
    It is not only known whether or not there is a ship there, but also the
    'shape' of that ship - whether it is a singleton, the middle of a ship, or
    the end of a ship, extending up, right, down, or left.
    """
    INVISIBLE = -1
    WATER = 0
    SINGLETON = 1
    MIDDLE = 2
    END_UP = 3
    END_RIGHT = 4
    END_DOWN = 5
    END_LEFT = 6

class Ocean:
    def __init__(self, grid: list[list[bool]], mask: list[list[bool]] = None):
        """
        Create an ocean with the given 2D Boolean grid of whether a ship is in
        each position. Also provide an optional mask indicating which cells are
        given to the player (as either ship or water) at the start of a game. If
        not provided, no cells are given. An AssertionError will be thrown if
        either is invalid.
        """

        # Validate grid
        self.grid = grid
        try:
            self.height = len(grid)
            self.width = len(grid[0])
            for row in grid:
                assert len(row) == self.width, "All rows in grid must have same width"
                for index, cell in enumerate(row):
                    row[index] = bool(cell)

        except TypeError:
            assert False, "Grid must be an iterable containing iterables containing bools"

        assert 1 <= self.height <= 255 and 1 <= self.width <= 255, "Grid must be at least 1x1 and at most 255x255"

        # If mask not given, default to all cells invisible
        self.mask = mask
        if self.mask is None:
            self.mask = [[False] * self.width] * self.height

        # If given, validate
        else:
            try:
                assert len(self.mask) == self.height, "Mask must have same dimensions as grid"
                for row in self.mask:
                    assert len(row) == self.width, "Mask must have same dimensions as grid"
                    for index, cell in enumerate(row):
                        row[index] = bool(cell)

            except TypeError:
                assert False, "Mask must be an iterable containing iterables containing bools"

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
                            for c2 in range(max(c - 1, 0), min(c + size + 1, self.width)):
                                assert not grid_cp[r + 1][c2], f"Two ships adjacent around cell ({c2}, {r})!"

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
                            for r2 in range(r + 1, min(r + size + 1, self.height)):
                                assert not grid_cp[r2][c - 1], f"Two ships adjacent around cell ({c}, {r2})"
                        if c + 1 < self.width:
                            for r2 in range(r, min(r + size + 1, self.height)):
                                assert not grid_cp[r2][c + 1], f"Two ships adjacent around cell ({c}, {r2})"

                    # If neither then is a size 1 ship
                    else:
                        size = 1

                        # Check surrounding cells aren't ships
                        # Only have to check these as already checked top 3 and
                        # left 1 and if were directly right or down then
                        # wouldn't be in this else statement
                        if r + 1 < self.height:
                            if c > 0:
                                assert not grid_cp[r + 1][c - 1], f"Two ships adjacent around cell ({c}, {r})"
                            if c + 1 < self.width:
                                assert not grid_cp[r + 1][c + 1], f"Two ships adjacent around cell ({c}, {r})"

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

    def getVisibleGrid(self) -> list[list[VisibleCell]]:
        """
        Return the visible cells in the grid - a grid of the enum VisibleCell.
        """

        def calcVisibleCell(r: int, c: int) -> VisibleCell:
            if not self.mask[r][c]:
                return VisibleCell.INVISIBLE
            
            if not self.grid[r][c]:
                return VisibleCell.WATER

            up, right, down, left = False, False, False, False
            if r >= 1 and self.grid[r - 1][c]:
                up = True
            if c <= self.width - 2 and self.grid[r][c + 1]:
                right = True
            if r <= self.height - 2 and self.grid[r + 1][c]:
                down = True
            if c >= 1 and self.grid[r][c - 1]:
                left = True

            num_dirs = sum((up, right, down, left))
            if num_dirs == 0:
                return VisibleCell.SINGLETON
            if num_dirs == 2:
                return VisibleCell.MIDDLE
            
            assert num_dirs == 1, f"Two ships adjacent around cell ({c}, {r})"

            if up:
                return VisibleCell.END_UP
            if right:
                return VisibleCell.END_RIGHT
            if down:
                return VisibleCell.END_DOWN
            return VisibleCell.END_LEFT

        return [[calcVisibleCell(r, c) for c in range(self.width)] for r in range(self.height)]

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

    def __repr__(self):
        return f"Ocean(\n{self}\n)"

    def __eq__(self, other):
        """
        Return whether 'other' represents the same grid as this object.
        """
        if isinstance(other, Ocean):
            other = other.grid
        return other == self.grid

    def __hash__(self):
        """
        Return an integer uniquely representing the grid
        """

        # Convert the width and height into a 1-byte unsigned binary number - 
        # as each can be max 255
        bin_str = Util.intToUnsigned1Byte(self.width) + Util.intToUnsigned1Byte(self.height)

        # Add each cell to the bin string as a single bit
        for row in self.grid:
            for cell in row:
                if cell:
                    bin_str += "1"
                else:
                    bin_str += "0"

        # Convert to base 10
        return int(bin_str, base=2)
