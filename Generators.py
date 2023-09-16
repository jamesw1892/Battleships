#!/usr/bin/python3

"""
Functions to generate a Battleship grid. Each function must abide by the same
interface - it must take the desired width, height, and optionally fleet, and
output the grid. If a fleet is given then that number of each size ships must
be present. If fleet is None then any sized fleet can be used. If it is
impossible to create a valid grid with the number of ships of each size
determined by the fleet then raise a ValueError.
"""

import Game
import itertools
import random
import Util

def defaultFleet(width: int, height: int) -> dict[int, int]:
    """
    Return a normal fleet for the given size
    """
    return dict() # TODO

############################# EXHAUSTIVE GENERATOR #############################

def generateExhaustive(width: int, height: int, fleet: dict[int, int] | None = None) -> list[list[bool]]:
    """
    Yield possible Ocean grids of the given size.
    """

    # For each possible combination of cells:
    for cells in itertools.product((False, True), repeat=width*height):

        # Convert the 1D iterable of cells into a 2D grid
        grid = Util.make2D(cells, width)

        try:
            ocean = Game.Ocean(grid)

            # If it's valid and matches the desired fleet (if there is one) then
            # yield it
            if fleet is None or ocean.getFleet() == fleet:
                yield grid

        # If it isn't a valid grid then go round again
        except AssertionError:
            pass

################################## GENERATORS ##################################

def generateRandom(width: int, height: int, fleet: dict[int, int] | None = None) -> list[list[bool]]:
    """
    Generate a grid randomly. TODO: Currently hangs if it's impossible to make
    a valid grid with the given fleet.
    """

    while True:

        # Generate a width * height bit binary number
        bin_str = bin(random.randint(0, 2 ** (width * height) - 1))[2:]

        # Add leading zeros
        bin_str = "0" * (width * height - len(bin_str)) + bin_str

        # Make into the grid shape and convert to bool
        grid = [[digit == "1" for digit in row] for row in Util.make2D(bin_str, width)]

        try:
            ocean = Game.Ocean(grid)

            # If it's valid and matches the desired fleet (if there is one) then
            # return it
            if fleet is None or ocean.getFleet() == fleet:
                return grid

        # If it isn't a valid grid then go round again
        except AssertionError:
            pass
