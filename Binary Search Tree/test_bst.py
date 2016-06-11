#!/usr/bin/env python

import sys
import unittest

from bst import Node, BinarySearchTree
from problems import *

class BstTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BstTest, self).__init__(*args, **kwargs)
        self.tree = BinarySearchTree()
        self.bst = BinarySearchTree()
        self.empty_tree = BinarySearchTree()
        self.arr = [100, 20, 500, 30, 10, 40]

        for x in xrange(1, 6):
            self.bst.iterative_insert(x)

        for x in self.arr:
            self.tree.iterative_insert(x)

    def test_search(self):
        self.assertTrue(self.tree.iterative_search(30))
        self.assertFalse(self.tree.recursive_search(self.tree.get_root(), 12312))

    def test_size(self):
        self.assertEqual(self.tree.size(self.tree.get_root()), 6)
        self.assertEqual(self.bst.size(self.bst.get_root()), 5)
        self.assertEqual(self.empty_tree.size(self.empty_tree.get_root()), 0)

    def test_max_depth(self):
        self.assertEqual(self.tree.max_depth(self.tree.get_root()), 4)
        self.assertEqual(self.bst.max_depth(self.bst.get_root()), 5)

    def test_min(self):
        self.assertEqual(self.tree.get_min(self.tree.get_root()), 10)
        self.assertEqual(self.bst.get_min(self.bst.get_root()), 1)

    def test_max(self):
        self.assertEqual(self.tree.get_max(self.tree.get_root()), 500)
        self.assertEqual(self.bst.get_max(self.bst.get_root()), 5)

    def test_display(self):
        pass
        """
        print "Inorder Traversal: "
        self.tree.inorder(self.tree.get_root())
        print "Preorder Traversal: "
        self.tree.preorder(self.tree.get_root())
        print "Postorder Traversal: "
        self.tree.postorder(self.tree.get_root())
        """

    def test_remove(self):
        pass
        """
        self.tree.remove(self.tree.get_root(), 40)
        self.assertFalse(self.tree.iterative_search(40))
        self.tree.remove(self.tree.get_root(), 20)
        self.assertFalse(self.tree.iterative_searc(20))
        print "Inorder Traversal after removing 40: "
        self.tree.inorder(self.tree.get_root())
        """

    def test_level_order_traversal(self):
        pass
        """
        print "Level order traversal of first tree."
        self.tree.level_order_traversal()
        
        print "Level order traversal of second tree."
        self.bst.level_order_traversal()
        """

    def test_max_width(self):
        pass
        """
        self.assertEqual(self.tree.max_width(), 2)
        self.assertEqual(self.bst.max_width(), 2)
        self.assertEqual(self.empty_tree(), 0)
        """

    def test_nodes_at_distance(self):
        self.tree.nodes_at_distance(self.tree.get_root(), 3)

    def test_identical(self):
        self.tree2 = BinarySearchTree()
        for x in self.arr:
            self.tree2.iterative_insert(x)

        self.assertTrue(self.tree.get_root(), self.tree2.get_root())

    def test_leafcount(self):
        self.assertEqual(self.tree.count_leafs(self.tree.get_root()), 3)

if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
