#!/usr/bin/python3

"""
Functions to generate a Battleship grid. Each function must abide by the same
interface - it must take the desired width, height, and optionally fleet, and
output the grid. If a fleet is given then that number of each size ships must
be present. If fleet is None then the default fleet for that size will be used
as output by the defaultFleet function. If it is impossible to create a valid
grid with the number of ships of each size determined by the fleet then raise
a ValueError.
"""

def defaultFleet(width: int, height: int) -> dict[int, int]:
    """
    Return a normal fleet for the given size
    """
    return dict() # TODO

################################## GENERATORS ##################################

def generateRandom(width: int, height: int, fleet: dict[int, int] | None) -> list[list[bool]]:
    """
    Generate a grid randomly.
    """
    return [[True]] # TODO
