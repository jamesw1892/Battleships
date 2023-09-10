#!/usr/bin/python3

"""
Tests.
"""

import Game
import Solvers
import Util
import unittest

GRID_VALID_1 = [
    [1, 0, 1],
    [0, 0, 1],
    [1, 0, 1]
]

GRID_VALID_2 = [
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

GRID_INVALID_1 = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 0, 1]
]

GRID_INVALID_2 = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 0, 1]
]

GRID_INVALID_3 = [
    [1, 0, 1],
    [0, 0, 1],
    [1, 1, 1]
]

GRID_INVALID_4 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

GRID_INVALID_5 = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 0]
]

class TestGame(unittest.TestCase):
    def test_init_1(self):
        Game.Ocean(GRID_VALID_1)

    def test_width_1(self):
        self.assertEqual(Game.Ocean(GRID_VALID_1).getWidth(), 3)

    def test_height_1(self):
        self.assertEqual(Game.Ocean(GRID_VALID_1).getHeight(), 3)

    def test_rowNums_1(self):
        self.assertEqual(Game.Ocean(GRID_VALID_1).getRowNums(), [2, 1, 2])

    def test_colNums_1(self):
        self.assertEqual(Game.Ocean(GRID_VALID_1).getColNums(), [2, 0, 3])

    def test_fleet_1(self):
        self.assertEqual(Game.Ocean(GRID_VALID_1).getFleet(), {1: 2, 3: 1})

    def test_init_2(self):
        Game.Ocean(GRID_VALID_2)

    def test_width_2(self):
        self.assertEqual(Game.Ocean(GRID_VALID_2).getWidth(), 15)

    def test_height_2(self):
        self.assertEqual(Game.Ocean(GRID_VALID_2).getHeight(), 15)

    def test_rowNums_2(self):
        self.assertEqual(Game.Ocean(GRID_VALID_2).getRowNums(), [3, 2, 1, 1, 4, 1, 3, 8, 1, 2, 0, 1, 1, 5, 2])

    def test_colNums_2(self):
        self.assertEqual(Game.Ocean(GRID_VALID_2).getColNums(), [4, 2, 1, 2, 2, 2, 2, 1, 4, 4, 5, 2, 1, 2, 1])

    def test_fleet_2(self):
        self.assertEqual(Game.Ocean(GRID_VALID_2).getFleet(), {1: 5, 2: 4, 3: 3, 4: 2, 5: 1})

    def test_invalid_1(self):
        self.assertRaises(AssertionError, Game.Ocean, GRID_INVALID_1)

    def test_invalid_2(self):
        self.assertRaises(AssertionError, Game.Ocean, GRID_INVALID_2)

    def test_invalid_3(self):
        self.assertRaises(AssertionError, Game.Ocean, GRID_INVALID_3)

    def test_invalid_4(self):
        self.assertRaises(AssertionError, Game.Ocean, GRID_INVALID_4)

    def test_invalid_5(self):
        self.assertRaises(AssertionError, Game.Ocean, GRID_INVALID_5)

    def test_equal_1obj_1obj(self):
        self.assertTrue(Game.Ocean(GRID_VALID_1) == Game.Ocean(GRID_VALID_1))

    def test_equal_1obj_1list(self):
        self.assertTrue(Game.Ocean(GRID_VALID_1) == GRID_VALID_1)

    def test_equal_1list_1obj(self):
        self.assertTrue(GRID_VALID_1 == Game.Ocean(GRID_VALID_1))

    def test_equal_1obj_2obj(self):
        self.assertFalse(Game.Ocean(GRID_VALID_1) == Game.Ocean(GRID_VALID_2))

    def test_equal_1obj_2list(self):
        self.assertFalse(Game.Ocean(GRID_VALID_1) == GRID_VALID_2)

    def test_equal_1list_2obj(self):
        self.assertFalse(GRID_VALID_1 == Game.Ocean(GRID_VALID_2))

    def test_equal_2obj_1obj(self):
        self.assertFalse(Game.Ocean(GRID_VALID_2) == Game.Ocean(GRID_VALID_1))

    def test_equal_2obj_1list(self):
        self.assertFalse(Game.Ocean(GRID_VALID_2) == GRID_VALID_1)

    def test_equal_2list_1obj(self):
        self.assertFalse(GRID_VALID_2 == Game.Ocean(GRID_VALID_1))

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
    # Solvers.solve(Solvers.dummySolver, Game.Ocean(GRID_VALID_2))
    unittest.main()
