#!/usr/bin/python

# This is a linked list representation of a Queue.

import sys

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue(object):
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def put(self, item):
        nd = Node(item)
        if self.rear is None:
            self.rear = nd
            self.front = nd
        else:
            self.rear.next_node = nd
            self.rear = nd

    def get(self):
        if self.front is None and self.rear is None:
            print "Queue is empty."
        else:
            data = self.front.data
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next_node

            print data

    def is_empty(self):
        return self.front is None and self.rear is None


if __name__ == '__main__':
    queue = Queue()
    for i in xrange(1, 11):
        queue.put(i)

    while not queue.is_empty():
        queue.get()

    sys.exit(0)
