#!/usr/bin/python

# This is an array based implementation of a Queue.

import sys

class Queue(object):
    def __init__(self, max_size=0):
        self.size = max_size
        self.arr = []

    def enqueue(self, item):
        '''Enqueue an element.'''
        if self.is_full():
            print "Queue is full."
        else:
            self.arr.append(item)

    def dequeue(self):
        '''Pop an item.'''
        if self.is_empty():
            print "Queue is empty."
        else:
            self.arr.pop(0)

    def is_empty(self):
        '''Return if the Queue is empty or not.'''
        return len(self.arr) == 0

    def is_full(self):
        '''Return if the Queue is full or not.'''
        return len(self.arr) == self.size

    def front(self):
        '''Return the front item.'''
        if self.is_empty():
            print "Queue is empty."
        else:
            print self.arr[0]

    def rear(self):
        '''Return the rear item.'''
        if self.is_empty():
            print "Queue is empty."
        else:
            print self.arr[len(self.arr)-1]

if __name__ == '__main__':
    queue = Queue(10)
    for i in xrange(1, 11):
        queue.enqueue(i)

    while not queue.is_empty():
        queue.front()
        queue.dequeue()

    sys.exit(0)
