import unittest
from src.laba7_def_Boyer_Moore import *

class TestBoyerMoore(unittest.TestCase):
    def test_single_match(self):
        haystack = "this is a example for test title"
        needle = "example"
        result = boyer_moore(haystack, needle)
        self.assertEqual(result, 10)

    def test_ukr_lg(self):
        haystack = "тут має бути тестовий текст для перевірки"
        needle = "текст"
        result = boyer_moore(haystack, needle)
        self.assertEqual(result, 22)

    def test_no_match(self):
        haystack = "this is a simple example"
        needle = "test"
        result = boyer_moore(haystack, needle)
        self.assertEqual(result, -1)

    def test_multiple_matches(self):
        haystack = "example example example"
        needle = "example"
        result = boyer_moore(haystack, needle)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()