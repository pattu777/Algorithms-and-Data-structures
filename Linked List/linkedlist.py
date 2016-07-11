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

    def rotate(self, k):
        """Left rotate the linked list by k items."""
        if self.head is None or k == 0:
            return
        else:
            current = self.head
            prev_head = self.head
            prev = None
            count = 0

            # Skip through the first k items and fetch the last one.
            while current is not None and count < k:
                prev = current
                current = current.next_node
                count += 1

            # Make the current node as head.
            self.head = current

            # Fetch the end node.
            while current.next_node is not None:
                current = current.next_node

            # Point the next pointer of the end node to the previous head
            current.next_node = prev_head

            # Make the next pointer of prev node to None.
            prev.next_node = None

    def make_loop(self):
        """Make a loop in a linked list. Point the last node to the second node."""
        if self.head is not None:
            nd = self.head
            while nd.next_node is not None:
                nd = nd.next_node

            nd.next_node = self.head.next_node

    def detect_loop(self):
        """Detect a loop in a singly linked list."""
        slow_ptr = self.head
        fast_ptr = self.head

        while slow_ptr and fast_ptr and fast_ptr.next_node:
            slow_ptr = slow_ptr.next_node
            fast_ptr = fast_ptr.next_node.next_node

            if slow_ptr == fast_ptr:
                return True

        return False

    def remove_loop(self):
        pass

    def kth_from_head(self, k):
        """Return the kth node from the head."""
        if self.head is not None and k != 0:
            nd = self.head
            count = 0
            while nd is not None:
                count += 1
                if count == k:
                    return nd.data
                nd = nd.next_node

            if count < k:
                print "K is out of range"


    def kth_from_end(self, k):
        """Return the kth node from end."""
        if self.head is not None and k != 0:
            nd = self.head
            count = 0
            num_nodes = self.size()
            while nd is not None:
                count += 1
                if count == num_nodes-k+1:
                    return nd.data
                nd = nd.next_node

    def kth_from_tail(self, k):
        """Return the kth node from end using two pointers."""
        if self.head is not None and k != 0:
            ptr1 = ptr2 = self.head
            count = 0
            while count != k:
                ptr1 = ptr1.next_node
                count += 1
            
            while ptr1 is not None:
                ptr1 = ptr1.next_node
                ptr2 = ptr2.next_node

            return ptr2.data    


    def delete(self):
        """Delete the entire linked list.

        Method 1:
        =========
        if head is not None:
            Traverse the list node by node.
            Make each individual node None.
            
        Method 2:
        =========
        if head is not None:
            Make head None

        """
        if self.head is not None:
            self.head = None

    def count_item(self, item):
        """Count the number of times an item occurs in the list."""
        if self.head is None:
            return 0
        else:
            nd = self.head
            count = 0
            while nd is not None:
                if nd.data == item:
                    count += 1
                nd = nd.next_node

            return count
            

    def is_pallindrome(self):
        """Check if the linked list is a pallindrome or not."""
        if self.head is None:
            return True
        else:
            val = True
            # Get the size of the linked list.
            count = self.size()

            # Find the middle element.
            middle = self.get_middle()

            # Reverse the first half of the linked list.
            beg_second = middle.next_node
            middle.next_node = None
            self.reverse(self.head)

            ptr1 = self.head
            ptr2 = beg_second

            while ptr1 and ptr2:
                if ptr1.data != ptr2.data:
                    val = False
                    break

            # Reverse back the first half.
            self.reverse(self.head)

            # Find the last element of the first half.
            nd = self.head
            while nd.next_node is not None:
                nd = nd.next_node

            # Link the first and second half.
            nd.next_node = beg_second

            return val

