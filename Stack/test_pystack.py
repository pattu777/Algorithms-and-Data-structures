#!/usr/bin/python

import sys
import unittest

from pystack import Stack
from problems import is_balanced, reverse_string

class TestStack(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestStack, self).__init__(*args, **kwargs)
        self.stack = Stack(100)
        for i in xrange(0, 10):
            self.stack.push(i)

    def test_length(self):
        # Test the length of the stack.
        self.assertEqual(self.stack.length(), 10)

    def test_push(self):
        # Test push operation.
        self.stack.push(191)
        self.assertEqual(self.stack.peek(), 191)
        self.assertEqual(self.stack.length(), 11)

    def test_peek(self):
        # Test peek operation.
        self.assertEqual(self.stack.peek(), 9)

    def test_pop(self):
        # Test pop operation.
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 8)
        self.assertEqual(self.stack.length(), 9)

    def test_paranthesis(self):
        """Test if a set of paranthesis is balanced or not."""
        self.assertTrue(is_balanced("(((())))"))
        self.assertFalse(is_balanced("(("))
        self.assertTrue(is_balanced("()()()"))
        self.assertFalse(is_balanced(")"))
        self.assertTrue(is_balanced("()(())(((())))"))
        self.assertTrue(is_balanced("[()]{}{[()()]()}"))
        self.assertFalse(is_balanced("[(])"))
        self.assertFalse(is_balanced("}"))

    def test_reverse(self):
        self.assertEqual("abcde", reverse_string("edcba"))
        self.assertEqual("1", reverse_string("1"))
        self.assertEqual("", reverse_string(""))
        self.assertFalse("123412131" == reverse_string("12341231"))
        self.assertEqual("anna", reverse_string("anna"))

if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
