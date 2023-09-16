#!/usr/bin/python3

"""
Functions to generate a Battleship grid. Each function must abide by the same
interface - it must take the desired width, height, and optionally fleet, and
output the grid. If a fleet is given then that number of each size ships must
be present. If fleet is None then the default fleet for that size will be used
as output by the defaultFleet function. If it is impossible to create a valid
grid with the number of ships of each size determined by the fleet then raise
a ValueError.

The only exception is generateExhaustive which generates all possible grids of
the given size so does not take a fleet.
"""

import Game
import itertools
import Util

def defaultFleet(width: int, height: int) -> dict[int, int]:
    """
    Return a normal fleet for the given size
    """
    return dict() # TODO

############################# EXHAUSTIVE GENERATOR #############################

def generateExhaustive(width: int, height: int):
    """
    Yield possible Ocean grids of the given size.
    """

    # For each possible combination of cells:
    for cells in itertools.product((False, True), repeat=width*height):

        # Convert the 1D iterable of cells into a 2D grid
        grid = Util.make2D(cells, width)

        # Instantiate Ocean and if valid, yield
        try:
            yield Game.Ocean(grid)
        except AssertionError:
            pass

################################## GENERATORS ##################################

def generateRandom(width: int, height: int, fleet: dict[int, int] | None) -> list[list[bool]]:
    """
    Generate a grid randomly.
    """
    return [[True]] # TODO
