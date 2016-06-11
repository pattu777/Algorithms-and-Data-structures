#!/usr/bin/env python

# Circular Linked List implementation.

class Node(object):
	def __init__(self, data=0, next_node=None):
		self.data = data
		self.next_node = next_node

class CircularLinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert(self, item):
		"""Insert an element into the circular linked list."""
		nd = Node(item)
		current = self.head

		if self.head is not None:
			while current.next_node != self.head:
				current = current.next_node
			current.next_node = nd
			nd.next_node = self.head

		else:
			nd.next_node = nd 

		self.head = nd

	def print_list(self):
		"""Display the elements of the circular linked list."""
		tmp = self.head
		if self.head is not None:
		    while True:
		        print "%d" % (tmp.data),
		        tmp = tmp.next_node
		        if tmp == self.head:
		            break

	def sorted_insert(self, item):
		"""Insert an item into a sorted circular linked list."""
		if self.head is None:
			self.insert(item)
		else:
			current = self.head
			while current.next_node is not self.head and current.data < item:
				current = current.next_node

			nd = Node(current.data)
			current.data = item
			nd.next_node = current.next_node
			current.next_node = nd


if __name__ == '__main__':
	clist = CircularLinkedList()
	for x in xrange(100):
		clist.insert(100-x)

	clist.print_list()
	#for x in xrange(11, 100):
		#clist.sorted_insert(x)
	#clist.print_list()