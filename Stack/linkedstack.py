#!/usr/bin/python

import sys

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, item):
        new_node = Node(item)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next_node = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print "Stack is already empty."
        else:
            nd = self.top.next_node
            self.top = nd

    def peek(self):
        if self.top is None:
            print "Stack is empty."
        else:
            print self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        if self.top is None:
            return 0
        else:
            nd = self.top
            size = 0
            while nd is not None:
                nd = nd.next_node
                size += 1
            return size

if __name__ == '__main__':
    stack = Stack()
    for i in xrange(1, 11):
        stack.push(i)

    print stack.size()
    while not stack.is_empty():
        stack.peek()
        stack.pop()

    sys.exit(0)
