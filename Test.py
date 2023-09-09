#!/usr/bin/python3

"""
Tests.
"""

import Game
import Solvers
import Util
import unittest

# Valid 3x3
INIT_1 = [
    [1, 0, 1],
    [0, 0, 1],
    [1, 0, 1]
]

# Valid 15x15
INIT_2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
]

class TestGame(unittest.TestCase):
    def test_init_1(self):
        Game.Ocean(INIT_1)

    def test_width_1(self):
        self.assertEqual(Game.Ocean(INIT_1).getWidth(), 3)

    def test_height_1(self):
        self.assertEqual(Game.Ocean(INIT_1).getHeight(), 3)

    def test_rowNums_1(self):
        self.assertEqual(Game.Ocean(INIT_1).getRowNums(), [2, 1, 2])

    def test_colNums_1(self):
        self.assertEqual(Game.Ocean(INIT_1).getColNums(), [2, 0, 3])

    def test_init_2(self):
        Game.Ocean(INIT_2)

    def test_width_2(self):
        self.assertEqual(Game.Ocean(INIT_2).getWidth(), 15)

    def test_height_2(self):
        self.assertEqual(Game.Ocean(INIT_2).getHeight(), 15)

    def test_rowNums_2(self):
        self.assertEqual(Game.Ocean(INIT_2).getRowNums(), [3, 2, 1, 1, 4, 1, 3, 8, 1, 2, 0, 1, 1, 5, 2])

    def test_colNums_2(self):
        self.assertEqual(Game.Ocean(INIT_2).getColNums(), [4, 2, 1, 2, 2, 2, 2, 1, 4, 4, 5, 2, 1, 2, 1])

class TestUtil(unittest.TestCase):
    def test_pad_centre_not_required(self):
        self.assertEqual(Util.padCentre("hi", 2), "hi")
    def test_pad_centre_int(self):
        self.assertEqual(Util.padCentre(1, 1), "1")
    def test_pad_centre_1_needed(self):
        self.assertEqual(Util.padCentre("hi", 3), "hi ")
    def test_pad_centre_2_needed(self):
        self.assertEqual(Util.padCentre("hi", 4), " hi ")
    def test_pad_centre_short(self):
        self.assertEqual(Util.padCentre("hi", 1), "hi")

if __name__ == "__main__":
    # Solvers.solve(Solvers.dummySolver, Game.Ocean(INIT_2))
    unittest.main()
