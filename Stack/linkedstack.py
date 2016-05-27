#!/usr/bin/python

import sys

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack(object):
    def __init__(self, size=0, top=None):
        self.size = size
        self.top = top

    def push(self, item):
        nd = self.top
        current_length = 0

        while nd is not None:
            nd = nd.next_node
            current_length += 1

        if current_length == self.size:
            print "Stack is full."
        else:
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

    def length(self):
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
    stack = Stack(10)
    for i in xrange(1, 11):
        stack.push(i)

    print stack.length()
    while not stack.is_empty():
        stack.peek()
        stack.pop()

    sys.exit(0)
