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

    def test_invalid_none(self):
        self.assertRaises(AssertionError, Game.Ocean, None)

    def test_invalid_no_outer_iterable(self):
        self.assertRaises(AssertionError, Game.Ocean, Game.Ocean(GRID_VALID_1))

    def test_invalid_no_inner_iterable(self):
        self.assertRaises(AssertionError, Game.Ocean, [Game.Ocean(GRID_VALID_1)])

    def test_invalid_empty(self):
        self.assertRaises(AssertionError, Game.Ocean, [[]])

    def test_invalid_too_wide(self):
        self.assertRaises(AssertionError, Game.Ocean, [[False] * 256])

    def test_invalid_too_high(self):
        self.assertRaises(AssertionError, Game.Ocean, [[False]] * 256)

    def test_invalid_inconsistent_widths(self):
        self.assertRaises(AssertionError, Game.Ocean, [[False], [False, False]])

    def test_invalid_ships_adjacent_1(self):
        self.assertRaises(AssertionError, Game.Ocean, [
            [1, 0, 1],
            [0, 1, 1],
            [1, 0, 1]
        ])

    def test_invalid_ships_adjacent_2(self):
        self.assertRaises(AssertionError, Game.Ocean, [
            [1, 1, 1],
            [0, 0, 1],
            [1, 0, 1]
        ])

    def test_invalid_ships_adjacent_3(self):
        self.assertRaises(AssertionError, Game.Ocean, [
            [1, 0, 1],
            [0, 0, 1],
            [1, 1, 1]
        ])

    def test_invalid_ships_adjacent_4(self):
        self.assertRaises(AssertionError, Game.Ocean, [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])

    def test_invalid_ships_adjacent_5(self):
        self.assertRaises(AssertionError, Game.Ocean, [
            [0, 0, 1],
            [0, 1, 0],
            [0, 0, 0]
        ])

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

    def test_hash_1(self):
        self.assertEqual(hash(Game.Ocean(GRID_VALID_1)), int("0000001100000011101001101", base=2))

    def test_hash_2(self):
        self.assertEqual(hash(Game.Ocean(GRID_VALID_2)), hash(int("0000111100001111000000001011000100000001000000000000001000000000000001000000000111000010000000000000010000111000000000000000011100011111100000000000000000100000010000000000000000000000000000100000000000000100000110000110100000000000000100010", base=2)))

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
    def test_intToUnsigned1Byte_neg1(self):
        self.assertRaises(AssertionError, Util.intToUnsigned1Byte, -1)
    def test_intToUnsigned1Byte_256(self):
        self.assertRaises(AssertionError, Util.intToUnsigned1Byte, 256)
    def test_intToUnsigned1Byte_0(self):
        self.assertEqual(Util.intToUnsigned1Byte(0), "00000000")
    def test_intToUnsigned1Byte_1(self):
        self.assertEqual(Util.intToUnsigned1Byte(1), "00000001")
    def test_intToUnsigned1Byte_2(self):
        self.assertEqual(Util.intToUnsigned1Byte(2), "00000010")
    def test_intToUnsigned1Byte_3(self):
        self.assertEqual(Util.intToUnsigned1Byte(3), "00000011")
    def test_intToUnsigned1Byte_255(self):
        self.assertEqual(Util.intToUnsigned1Byte(255), "11111111")

if __name__ == "__main__":
    # Solvers.solve(Solvers.dummySolver, Game.Ocean(GRID_VALID_2))
    unittest.main()
