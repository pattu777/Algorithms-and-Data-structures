#!/usr/bin/env python

import sys
import unittest

from linkedlist import Node, LinkedList

class LinkedTestClass(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LinkedTestClass, self).__init__(*args, **kwargs)
        self.custom_list = LinkedList()
        for x in xrange(1, 100):
            self.custom_list.insert_at_tail(x)

    def test_size(self):
        """Test size operation."""
        self.assertEqual(self.custom_list.size(), 99)

    def test_get_middle(self):
        '''Test middle operation.'''
        self.assertEqual(self.custom_list.get_middle(), 50)

    def test_reverse(self):
        '''Test reverse operation.'''
        self.custom_list.reverse()
        self.reversed_list = LinkedList()
        for x in xrange(1, 100):
            self.reversed_list.insert_at_head(x)
        nd1 = self.custom_list.head
        nd2 = self.reversed_list.head

        while nd1 is not None and nd2 is not None:
            self.assertEqual(nd1.data, nd2.data)
            nd1 = nd1.next_node
            nd2 = nd2.next_node

    def test_insert_at_head(self):
        ''' Test insert_at_head operation. '''
        self.custom_list.insert_at_head(1001)
        self.assertEqual(self.custom_list.head.data, 1001)


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
