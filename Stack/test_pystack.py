#!/usr/bin/python

import sys
import unittest

from pystack import Stack

class TestStack(unittest.TestCase):
    def test(self):
        self.stack = Stack(100)
        for i in xrange(0, 10):
            self.stack.push(i)

        # Test the length of the stack.
        self.assertEqual(self.stack.length(), 10)

        # Test push operation.
        self.stack.push(191)
        self.assertEqual(self.stack.peek(), 191)
        self.assertEqual(self.stack.length(), 11)

        # Test peek operation.
        self.assertEqual(self.stack.peek(), 191)

        # Test pop operation.
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 9)
        self.assertEqual(self.stack.length(), 10)

if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
