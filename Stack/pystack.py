#!/usr/bin/python

# An array based implementation of a Stack.

import sys

class Stack(object):
    def __init__(self, size=0):
        self.size = size
        self.arr = []

    def push(self, item):
        """Push an item."""
        if self.is_full():
            print "Stack is full."
        else:
            self.arr.append(item)

    def pop(self):
        """Pop an item."""
        if self.is_empty():
            print "Stack is already empty."
        else:
            self.arr.pop()

    def peek(self):
        """Fetch the top item."""
        if self.is_empty():
            print "Stack is empty."
        else:
            return self.arr[len(self.arr)-1]

    def length(self):
        """Number of items in the stack."""
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return len(self.arr) == self.size
