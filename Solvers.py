#!/usr/bin/python3

"""
Functions to solve a Battleships game. Each function must abide by the same
interface - it must take the fleet, row numbers, and column numbers, and output
the grid. To run a solver, call the 'solve' function with the function of the
actual solver as the first argument and the Ocean instance as the second. This
will run the solver with the correct arguments, check the answer, and print it.
"""

import Game

def solve(solve_func, ocean: Game.Ocean):
    """
    Given a solver function and an ocean to solve, run the solver, check the
    answer, and print it.
    """

    grid = solve_func(ocean.getFleet(), ocean.getRowNums(), ocean.getColNums())

    if ocean == grid:
        print("Successfully solved:\n")
        print(ocean)
    else:
        print("Solved incorrectly. Correct answer:\n")
        print(ocean)
        print("\nAnswer given:\n")
        print("\n".join(" ".join("x" if cell else " " for cell in row) for row in grid))

################################### SOLVERS ####################################

def dummySolver(fleet: dict[int, int], row_nums: list[int], col_nums: list[int]) -> list[list[bool]]:
    return [[True]]
