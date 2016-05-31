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

    def enqueue(self, item):
        nd = Node(item)
        if self.rear is None:
            self.rear = nd
            self.front = nd
        else:
            self.rear.next_node = nd
            self.rear = nd

    def dequeue(self):
        if self.front is None:
            print "Queue is empty."
        else:
            nd = self.front
            self.front = self.front.next_node
            while self.front is None:
                self.rear = None

            print nd.data

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return self.rear is not None and self.front == self.rear


if __name__ == '__main__':
    queue = Queue()
    for i in xrange(1, 11):
        queue.enqueue(i)

    while not queue.is_empty():
        queue.dequeue()

    sys.exit(0)
