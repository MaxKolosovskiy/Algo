import unittest
from src.kruskals_algorithm import *


class TestUnionFind(unittest.TestCase):
    def test_find(self):
        uf = UnionFind(5)
        self.assertEqual(uf.find(0), 0)
        self.assertEqual(uf.find(4), 4)

    def test_union(self):
        uf = UnionFind(5)
        self.assertTrue(uf.union(0, 1))
        self.assertEqual(uf.find(1), 0)

        self.assertFalse(uf.union(0, 1))
        self.assertTrue(uf.union(1, 2))
        self.assertEqual(uf.find(2), 0)

    def test_union_rank(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(2, 3)
        self.assertTrue(uf.union(1, 3))
        self.assertEqual(uf.rank[uf.find(0)], 2)

if __name__ == '__main__':
    unittest.main()