import unittest
from src.laba6_alg_max_career_exp import *
class TestMaxExperience(unittest.TestCase):
    def test_example_1(self):
        levels = 4
        experience = [[4], [3, 1], [2, 1, 5], [1, 3, 2, 1]]
        self.assertEqual(max_experience(levels, experience), 12)

    def test_example_2(self):
        levels = 1
        experience = [[9999]]
        self.assertEqual(max_experience(levels, experience), 9999)

    def test_example_3(self):
        levels = 5
        experience = [[0], [1, 1], [0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1, 0]]
        self.assertEqual(max_experience(levels, experience), 3)