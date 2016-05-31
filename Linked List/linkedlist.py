#!/usr/bin/python

import sys

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next=None):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None, size=0):
        self.head = head

    def insert_at_head(self, data):
        ptr = Node(data)
        ptr.set_next(self.head)
        self.head = ptr

    def insert_at_tail(self, data):
        if self.head is None:
            self.insert_at_head(data)
        else:
            ptr = Node(data)
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(ptr)

    def print_list(self):
        if self.head is None:
            return
        else:
            ptr = self.head
            while ptr:
                print ptr.data, " ",
                ptr = ptr.get_next()
            print ""

    def remove_from_head(self):
        if self.head is None:
            return
        else:
            ptr = self.head
            self.head = self.head.get_next()
            del ptr

    def remove_from_tail(self):
        if self.head is None:
            return
        elif self.head.get_next() is None:
            self.head = None
        else:
            current = self.head
            while current.get_next().get_next() is not None:
                current = current.get_next()
            ptr = current.get_next()
            current.set_next()
            del ptr

    def size(self):
        if self.head is None:
            return 0
        else:
            current = self.head
            count = 0
            while current is not None:
                current = current.get_next()
                count += 1
            return count

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            tmp = current.get_next()
            current.set_next(prev)
            prev = current
            current = tmp
        self.head = prev

    def get_middle(self):
        slow_ptr = fast_ptr = self.head
        if self.head is None:
            print "List is empty."
        else:
            while fast_ptr.get_next() is not None and fast_ptr.get_next().get_next() is not None:
                slow_ptr = slow_ptr.get_next()
                fast_ptr = fast_ptr.get_next().get_next()
            return slow_ptr.get_data()

if __name__ == "__main__":
    ll = LinkedList()
    for x in xrange(1, 10):
        ll.insert_at_tail(x)

    ll.print_list()
    ll.reverse()
    ll.print_list()
    print ll.get_middle()

    sys.exit(0)
