import unittest
from laba1 import is_array_monotonic

class Testlab1(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(is_array_monotonic([1, 4, 7, 7, 15]))

    def test_decreasing(self):
        self.assertTrue(is_array_monotonic([10, 8, 4, 1]))

    def test_not_monotonic(self):
        self.assertFalse(is_array_monotonic([1, 5, 2, 4, 15]))

    def test_is_array_monotoniс(self):
        self.assertTrue(is_array_monotonic([7]))

    def test_none(self):
        self.assertTrue(is_array_monotonic([]))

    def test_increasing_v2(self):
        self.assertTrue(is_array_monotonic([2, 2, 2, 2, 2, 3]))

    def test_decreasing_v2(self):
        self.assertTrue(is_array_monotonic([2, 2, 2, 2, 2, 1]))

    def test_decreasing_v3(self):
        self.assertTrue(is_array_monotonic([1, 1, 1, 1, 1, 0]))
