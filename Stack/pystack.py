#!/usr/bin/python

# An array based implementation of a Stack.

import sys

class Stack(object):
    def __init__(self, size):
        self.size = size
        self.arr = []
        self.current_length = 0

    def push(self, item):
        if self.current_length == self.size:
            print "Stack is full."
        else:
            self.arr.append(item)
            self.current_length += 1

    def pop(self):
        if self.current_length == 0:
            print "Stack is already empty."
        else:
            self.arr.pop()
            self.current_length -= 1

    def peek(self):
        if self.current_length == 0:
            print "Stack is empty."
        else:
            return self.arr[self.current_length-1]

    def length(self):
        return self.current_length

    def is_empty(self):
        return self.current_length == 0

    def is_full(self):
        return self.size == self.current_length

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

