import unittest
from src.electricians import *

class TestWireLengthCalculator(unittest.TestCase):
    def test_calculate_wire_length_example_1(self):
        w = 2
        heights = [3, 3, 3]
        expected_length = 5.65
        self.assertAlmostEqual(calculate_length(heights, w), expected_length, delta=0.01)

    def test_calculate_wire_length_example_2(self):
        w = 100
        heights = [1, 1, 1, 1]
        expected_length = 300.0
        self.assertAlmostEqual(calculate_length(heights, w), expected_length, delta=0.01)

    def test_calculate_wire_length_example_3(self):
        w = 4
        heights = [100, 2, 100, 2, 100]
        expected_length = 396.32
        self.assertAlmostEqual(calculate_length(heights, w), expected_length, delta=0.01)

if __name__ == '__main__':
    unittest.main()