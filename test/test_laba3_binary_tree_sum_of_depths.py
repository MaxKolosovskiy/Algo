import unittest
from src.laba3_binary_tree_sum_of_depths import *

class TestSumOfDepths(unittest.TestCase):
    def test_sum_of_depths(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(sum_of_depths(root), 10)

    def test_sum_of_depths_empty_tree(self):
        self.assertEqual(sum_of_depths(None), 0)

    def test_sum_of_depths_single_tree(self):
        root = TreeNode(1)
        self.assertEqual(sum_of_depths(root), 0)

    def test_sum_of_depths_left_left_left_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(sum_of_depths(root), 6)

    def test_sum_of_depths_right_right_right_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertEqual(sum_of_depths(root), 6)
