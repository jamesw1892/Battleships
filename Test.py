#!/usr/bin/python3

"""
Tests.
"""

import Game
import Generators
import Solvers
import Util
import unittest

GRID_VALID_1 = [
    [1, 0, 1],
    [0, 0, 1],
    [1, 0, 1]
]

GRID_VALID_1_MASK_1 = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 1, 0]
]

GRID_VALID_1_MASK_2 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

GRID_VALID_1_MASK_3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
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

    def test_visible_1_no_mask(self):
        self.assertEqual(Game.Ocean(GRID_VALID_1).getVisibleGrid(), [[None] * 3] * 3)

    def test_init_1_mask_1(self):
        Game.Ocean(GRID_VALID_1, GRID_VALID_1_MASK_1)

    def test_visible_1_mask_1(self):
        self.assertEqual(Game.Ocean(GRID_VALID_1, GRID_VALID_1_MASK_1).getVisibleGrid(), [
            [True, None , None],
            [None, None , None],
            [None, False, None]
        ])

    def test_init_1_mask_2(self):
        Game.Ocean(GRID_VALID_1, GRID_VALID_1_MASK_2)

    def test_visible_1_mask_2(self):
        self.assertEqual(Game.Ocean(GRID_VALID_1, GRID_VALID_1_MASK_2).getVisibleGrid(), GRID_VALID_1)

    def test_init_1_mask_3(self):
        Game.Ocean(GRID_VALID_1, GRID_VALID_1_MASK_3)

    def test_visible_1_mask_2(self):
        self.assertEqual(Game.Ocean(GRID_VALID_1, GRID_VALID_1_MASK_3).getVisibleGrid(), [[None] * 3] * 3)

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

    def test_visible_2_no_mask(self):
        self.assertEqual(Game.Ocean(GRID_VALID_2).getVisibleGrid(), [[None] * 15] * 15)

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

    def test_invalid_mask_no_outer_iterable(self):
        self.assertRaises(AssertionError, Game.Ocean, GRID_VALID_1, Game.Ocean(GRID_VALID_1))

    def test_invalid_mask_no_inner_iterable(self):
        self.assertRaises(AssertionError, Game.Ocean, GRID_VALID_1, [Game.Ocean(GRID_VALID_1)] * 3)

    def test_invalid_mask_diff_height_to_grid(self):
        self.assertRaises(AssertionError, Game.Ocean, GRID_VALID_1, [[False] * 3])

    def test_invalid_mask_diff_width_to_grid(self):
        self.assertRaises(AssertionError, Game.Ocean, GRID_VALID_1, [[False]] * 3)

    def test_invalid_mask_inconsistent_widths(self):
        self.assertRaises(AssertionError, Game.Ocean, GRID_VALID_1, [[False, False, False], [False, False], [False]])

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

    def test_make2D_valid_list_rectangle(self):
        self.assertEqual(Util.make2D([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
    def test_make2D_valid_list_uneven(self):
        self.assertEqual(Util.make2D([1, 2, 3], 2), [[1, 2], [3]])
    def test_make2D_valid_tuple_rectangle(self):
        self.assertEqual(Util.make2D((1, 2, 3, 4), 2), [[1, 2], [3, 4]])
    def test_make2D_valid_tuple_uneven(self):
        self.assertEqual(Util.make2D((1, 2, 3), 2), [[1, 2], [3]])
    def test_make2D_edge_empty_iterable(self):
        self.assertEqual(Util.make2D([], 2), [])
    def test_make2D_edge_iterable_smaller_width(self):
        self.assertEqual(Util.make2D([1], 2), [[1]])
    def test_make2D_invalid_not_iterable(self):
        self.assertRaises(TypeError, Util.make2D, Game.Ocean(GRID_VALID_1), 2)
    def test_make2D_invalid_not_int(self):
        self.assertRaises(TypeError, Util.make2D, [1, 2, 3, 4], "hi")
    def test_make2D_invalid_zero(self):
        self.assertRaises(ValueError, Util.make2D, [1, 2, 3, 4], 0)
    def test_make2D_invalid_neg(self):
        self.assertRaises(ValueError, Util.make2D, [1, 2, 3, 4], -1)

VALID_1x1_OCEANS = (
    [[False]],
    [[True]]
)
VALID_1x1_OCEANS_0 = (VALID_1x1_OCEANS[0],)
VALID_1x1_OCEANS_1 = (VALID_1x1_OCEANS[1],)

VALID_1x2_OCEANS = (
    [[False],
     [False]],
    [[False],
     [True ]],
    [[True ],
     [False]],
    [[True ],
     [True ]]
)
VALID_1x2_OCEANS_0 = (VALID_1x2_OCEANS[0],)
VALID_1x2_OCEANS_1 = (VALID_1x2_OCEANS[1], VALID_1x2_OCEANS[2])
VALID_1x2_OCEANS_2 = (VALID_1x2_OCEANS[3],)

VALID_2x1_OCEANS = (
    [[False, False]],
    [[False, True ]],
    [[True , False]],
    [[True , True ]]
)
VALID_2x1_OCEANS_0 = (VALID_2x1_OCEANS[0],)
VALID_2x1_OCEANS_1 = (VALID_2x1_OCEANS[1], VALID_2x1_OCEANS[2])
VALID_2x1_OCEANS_2 = (VALID_2x1_OCEANS[3],)

VALID_2x2_OCEANS = (
    [[False, False],
     [False, False]],
    [[False, False],
     [False, True ]],
    [[False, False],
     [True , False]],
    [[False, False],
     [True , True ]],
    [[False, True ],
     [False, False]],
    [[False, True ],
     [False, True ]],
    [[True , False],
     [False, False]],
    [[True , False],
     [True , False]],
    [[True , True ],
     [False, False]],
)
VALID_2x2_OCEANS_0 = (VALID_2x2_OCEANS[0],)
VALID_2x2_OCEANS_1 = (VALID_2x2_OCEANS[1], VALID_2x2_OCEANS[2], VALID_2x2_OCEANS[4], VALID_2x2_OCEANS[6])
VALID_2x2_OCEANS_2 = (VALID_2x2_OCEANS[3], VALID_2x2_OCEANS[5], VALID_2x2_OCEANS[7], VALID_2x2_OCEANS[8])

class TestGenerators(unittest.TestCase):
    def test_exhaustive_1_1_any(self):
        self.assertEqual(tuple(Generators.generateExhaustive(1, 1)), VALID_1x1_OCEANS)
    def test_exhaustive_1_1_fleet_0(self):
        self.assertEqual(tuple(Generators.generateExhaustive(1, 1, dict())), VALID_1x1_OCEANS_0)
    def test_exhaustive_1_1_fleet_1(self):
        self.assertEqual(tuple(Generators.generateExhaustive(1, 1, {1: 1})), VALID_1x1_OCEANS_1)
    def test_exhaustive_1_1_fleet_2(self):
        self.assertEqual(tuple(Generators.generateExhaustive(1, 1, {1: 2})), tuple())
    def test_exhaustive_1_2_any(self):
        self.assertEqual(tuple(Generators.generateExhaustive(1, 2)), VALID_1x2_OCEANS)
    def test_exhaustive_1_2_fleet_0(self):
        self.assertEqual(tuple(Generators.generateExhaustive(1, 2, dict())), VALID_1x2_OCEANS_0)
    def test_exhaustive_1_2_fleet_1(self):
        self.assertEqual(tuple(Generators.generateExhaustive(1, 2, {1: 1})), VALID_1x2_OCEANS_1)
    def test_exhaustive_1_2_fleet_2(self):
        self.assertEqual(tuple(Generators.generateExhaustive(1, 2, {2: 1})), VALID_1x2_OCEANS_2)
    def test_exhaustive_1_2_fleet_1_2(self):
        self.assertEqual(tuple(Generators.generateExhaustive(1, 2, {1: 2})), tuple())
    def test_exhaustive_2_1_any(self):
        self.assertEqual(tuple(Generators.generateExhaustive(2, 1)), VALID_2x1_OCEANS)
    def test_exhaustive_2_1_fleet_0(self):
        self.assertEqual(tuple(Generators.generateExhaustive(2, 1, dict())), VALID_2x1_OCEANS_0)
    def test_exhaustive_2_1_fleet_1(self):
        self.assertEqual(tuple(Generators.generateExhaustive(2, 1, {1: 1})), VALID_2x1_OCEANS_1)
    def test_exhaustive_2_1_fleet_2(self):
        self.assertEqual(tuple(Generators.generateExhaustive(2, 1, {2: 1})), VALID_2x1_OCEANS_2)
    def test_exhaustive_2_1_fleet_1_2(self):
        self.assertEqual(tuple(Generators.generateExhaustive(2, 1, {1: 2})), tuple())
    def test_exhaustive_2_2_any(self):
        self.assertEqual(tuple(Generators.generateExhaustive(2, 2)), VALID_2x2_OCEANS)
    def test_exhaustive_2_2_fleet_0(self):
        self.assertEqual(tuple(Generators.generateExhaustive(2, 2, dict())), VALID_2x2_OCEANS_0)
    def test_exhaustive_2_2_fleet_1(self):
        self.assertEqual(tuple(Generators.generateExhaustive(2, 2, {1: 1})), VALID_2x2_OCEANS_1)
    def test_exhaustive_2_2_fleet_2(self):
        self.assertEqual(tuple(Generators.generateExhaustive(2, 2, {2: 1})), VALID_2x2_OCEANS_2)
    def test_exhaustive_2_2_fleet_1_2(self):
        self.assertEqual(tuple(Generators.generateExhaustive(2, 2, {1: 2})), tuple())

    def test_random_1_1_any(self):
        self.assertIn(Generators.generateRandom(1, 1), VALID_1x1_OCEANS)
    def test_random_1_1_fleet_0(self):
        self.assertIn(Generators.generateRandom(1, 1, dict()), VALID_1x1_OCEANS_0)
    def test_random_1_1_fleet_1(self):
        self.assertIn(Generators.generateRandom(1, 1, {1: 1}), VALID_1x1_OCEANS_1)
    def test_random_1_2_any(self):
        self.assertIn(Generators.generateRandom(1, 2), VALID_1x2_OCEANS)
    def test_random_1_2_fleet_0(self):
        self.assertIn(Generators.generateRandom(1, 2, dict()), VALID_1x2_OCEANS_0)
    def test_random_1_2_fleet_1(self):
        self.assertIn(Generators.generateRandom(1, 2, {1: 1}), VALID_1x2_OCEANS_1)
    def test_random_1_2_fleet_2(self):
        self.assertIn(Generators.generateRandom(1, 2, {2: 1}), VALID_1x2_OCEANS_2)
    def test_random_2_1_any(self):
        self.assertIn(Generators.generateRandom(2, 1), VALID_2x1_OCEANS)
    def test_random_2_1_fleet_0(self):
        self.assertIn(Generators.generateRandom(2, 1, dict()), VALID_2x1_OCEANS_0)
    def test_random_2_1_fleet_1(self):
        self.assertIn(Generators.generateRandom(2, 1, {1: 1}), VALID_2x1_OCEANS_1)
    def test_random_2_1_fleet_2(self):
        self.assertIn(Generators.generateRandom(2, 1, {2: 1}), VALID_2x1_OCEANS_2)
    def test_random_2_2_any(self):
        self.assertIn(Generators.generateRandom(2, 2), VALID_2x2_OCEANS)
    def test_random_2_2_fleet_0(self):
        self.assertIn(Generators.generateRandom(2, 2, dict()), VALID_2x2_OCEANS_0)
    def test_random_2_2_fleet_1(self):
        self.assertIn(Generators.generateRandom(2, 2, {1: 1}), VALID_2x2_OCEANS_1)
    def test_random_2_2_fleet_2(self):
        self.assertIn(Generators.generateRandom(2, 2, {2: 1}), VALID_2x2_OCEANS_2)

if __name__ == "__main__":
    unittest.main()
