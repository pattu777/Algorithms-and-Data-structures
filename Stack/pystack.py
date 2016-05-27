#!/usr/bin/python

# An array based implementation of a Stack.

import sys

class Stack(object):
    def __init__(self, size):
        self.size = size
        self.arr = []

    def push(self, item):
        if self.is_full():
            print "Stack is full."
        else:
            self.arr.append(item)

    def pop(self):
        if self.is_empty():
            print "Stack is already empty."
        else:
            self.arr.pop()

    def peek(self):
        if self.is_empty():
            print "Stack is empty."
        else:
            return self.arr[len(self.arr)-1]

    def length(self):
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return len(self.arr) == self.size

if __name__ == '__main__':
    stack = Stack(10)
    for i in xrange(0, 10):
        stack.push(i)

    print stack.length()
    print stack.is_empty()
    print stack.is_full()

    while not stack.is_empty():
        print stack.peek()
        stack.pop()

    sys.exit(0)

