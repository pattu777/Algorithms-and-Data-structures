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
    def __init__(self, head=None):
        self.head = head

    def get_head(self):
        '''Return the head node.'''
        return self.head

    def get_next(self):
        pass

    def insert_at_head(self, data):
        '''Insert an element at the head of the list.'''
        ptr = Node(data)
        ptr.set_next(self.head)
        self.head = ptr

    def insert_at_tail(self, data):
        '''Insert an element at the end of the list.'''
        if self.head is None:
            self.insert_at_head(data)
        else:
            ptr = Node(data)
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(ptr)

    def print_list(self):
        '''Print all the elemenets.'''
        if self.head is None:
            return
        else:
            ptr = self.head
            while ptr:
                print ptr.data, " ",
                ptr = ptr.get_next()
            print ""

    def remove_from_head(self):
        '''Remove an element from the head.'''
        if self.head is None:
            return
        else:
            ptr = self.head
            self.head = self.head.get_next()
            del ptr

    def remove_from_tail(self):
        '''Remove an element from the tail.'''
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
        '''Get the number of elements.'''
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
        '''Reverse the linked list.'''
        current = self.head
        prev = None
        while current is not None:
            tmp = current.get_next()
            current.set_next(prev)
            prev = current
            current = tmp
        self.head = prev

    def get_middle(self):
        '''Get the middle element.'''
        slow_ptr = fast_ptr = self.head
        if self.head is None:
            print "List is empty."
        else:
            while fast_ptr.get_next() is not None and fast_ptr.get_next().get_next() is not None:
                slow_ptr = slow_ptr.get_next()
                fast_ptr = fast_ptr.get_next().get_next()
            return slow_ptr.get_data()

def merge_lists(ll1, ll2):
    '''Merge two sorted linked lists.'''
    if ll1.get_head() is None:
        return ll2
    elif ll2.get_head() is None:
        return ll1
    else:
        head1 = ll1.get_head()
        head2 = ll2.get_head()
        ll = LinkedList()

        while head1 is not None and head2 is not None:
            if head1 is not None and head1.data < head2.data:
                ll.insert_at_head(head1.data)
                head1 = head1.next_node
            elif head2 is not None and head1.data > head2.data:
                ll.insert_at_head(head2.data)
                head2 = head2.next_node

        return ll
