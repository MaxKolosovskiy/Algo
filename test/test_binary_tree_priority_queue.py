import unittest
from src.binary_tree_priority_queue import *

class TestTreePriority(unittest.TestCase):
    def test_insert(self):
        queue = PriorityQueue()
        queue.insert("CsGo2", 3)
        queue.insert("Dota2", 5)
        queue.insert("TheFinals", 1)
        self.assertEqual(str(queue), "**<TheFinals, CsGo2, Dota2>**")

    def test_none(self):
        queue = PriorityQueue()
        self.assertEqual(str(queue), "**<>**")

    def test_del_and_return_H_P(self):
        queue = PriorityQueue()
        queue.insert("Cola", 10)
        queue.insert("Fanta", 15)
        queue.insert("Tarxun", 5)
        self.assertEqual(queue.pop(), "Tarxun")
        self.assertEqual(str(queue), "**<Tarxun, Fanta>**")

    def test_peek(self):
        queue = PriorityQueue()
        queue.insert("AUDI", 12)
        queue.insert("BMW", 8)
        queue.insert("Mers", 14)
        self.assertEqual(queue.peek(), "Mers")
        self.assertEqual(str(queue), "**<BMW, AUDI, Mers>**")
