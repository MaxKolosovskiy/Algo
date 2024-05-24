import unittest
from src.electricians import *

class TestWireLengthFunctions(unittest.TestCase):

    def test_v1(self):
        distance = 2
        heights = [3, 3, 3]
        output_filename = "test_output_electricians.txt"
        result = compute_maximum_wire_length(distance, heights, output_filename)
        self.assertEqual(result, 5.66)

    def test_v2(self):
        distance = 100
        heights = [1, 1, 1, 1]
        output_filename = "test_output_electricians.txt"
        result = compute_maximum_wire_length(distance, heights, output_filename)
        self.assertEqual(result, 300)

    def test_v3(self):
        distance = 4
        heights = [100, 2, 100, 2, 100]
        output_filename = "test_output_electricians.txt"
        result = compute_maximum_wire_length(distance, heights, output_filename)
        self.assertEqual(result, 396.32)

    def test_v4(self):
        distance = 4
        heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
        output_filename = "test_output_electricians.txt"
        result = compute_maximum_wire_length(distance, heights, output_filename)
        self.assertEqual(result, 2738.18)


if __name__ == '__main__':
    unittest.main()