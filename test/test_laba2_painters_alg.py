import unittest
from src.laba2_painters_alg import main_paint_time

class TestMinPaintTime(unittest.TestCase):
    def test_example(self):
        K = 10
        T = 5
        L = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        self.assertEqual(main_paint_time(K, T, L), 100)

    def test_one_painter(self):
        K = 1
        T = 5
        L = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        self.assertEqual(main_paint_time(K, T, L), 700)

    def test_equal_l(self):
        K = 5
        T = 5
        L = [10, 10, 10, 10, 10]
        self.assertEqual(main_paint_time(K, T, L), 50)

    def test_empty_l(self):
        K = 3
        T = 5
        L = []
        self.assertEqual(main_paint_time(K, T, L), 0)
