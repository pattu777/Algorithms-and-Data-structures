#!/usr/bin/env python

import sys
import unittest

from linkedlist import Node, LinkedList, merge_lists

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

    def test_rotate(self):
        self.custom_list.rotate(5)
        #print "Rotated Linked List: "
        #self.custom_list.print_list()

    def test_loop(self):
        """Test loop in a linked list"""
        self.custom_list.make_loop()
        ll = LinkedList()
        for x in xrange(1000):
            ll.insert_at_tail(x)

        self.assertTrue(self.custom_list.detect_loop())
        self.assertFalse(ll.detect_loop())

    def test_kth(self):
        self.assertEqual(self.custom_list.kth_from_head(2), 2)
        self.assertEqual(self.custom_list.kth_from_head(19), 19)
        self.assertEqual(self.custom_list.kth_from_end(2), 98)
        self.assertEqual(self.custom_list.kth_from_tail(3), 97)
        self.assertEqual(self.custom_list.kth_from_tail(6), 94)

    def test_count_item(self):
        self.assertEqual(self.custom_list.count_item(11), 1)
        self.assertFalse(self.custom_list.count_item(19191) == 1)

    def test_delete(self):
        self.custom_list.delete()
        self.assertEqual(self.custom_list.size(), 0)

    def test_pallindrome(self):
        pass
        """
        self.ll1 = LinkedList()
        ll1.insert_at_tail(1)
        ll1.insert_at_tail(2)
        ll1.insert_at_tail(1)
        self.assertTrue(self.ll1.is_pallindrome())
        self.assertFalse(self.custom_list.is_pallindrome())
        self.assertTrue(LinkedList())
        """

if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
