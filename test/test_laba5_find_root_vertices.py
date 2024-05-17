import unittest
from src.laba5_find_root_vertices import *

class TestFindRootVertices(unittest.TestCase):
    def test_single_root_vertex(self):
        graph = [[1, 2], [], [3], []]
        expected_result = [0]
        self.assertEqual(find_root_vertices(graph), expected_result)


    def test_no_root_vertices(self):
        graph = [[1], [2], [0], [3]]
        expected_result = -1
        self.assertEqual(find_root_vertices(graph), expected_result)

    def test_large_graph(self):
        graph = [[1, 2], [3], [4], [], [5], [6], [7], [8], []]
        expected_result = [0]
        self.assertEqual(find_root_vertices(graph), expected_result)

    def test_cyclic_graph(self):
        graph = [[1], [2], [0]]
        expected_result = -1
        self.assertEqual(find_root_vertices(graph), expected_result)

if __name__ == '__main__':
    unittest.main()