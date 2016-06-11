#!/usr/bin/env python

# A python implementation of a Doubly Linked List.

class Node(object):
	def __init__(self, data=0, prev_node=None, next_node=None):
		self.data = data
		self.prev_node = prev_node
		self.next_node = next_node

class DoublyLinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert_at_front(self, item):
		"""Insert an item at the front of the list."""
		nd = Node(item)
		if self.head is None:
			self.head = nd
		else:
			nd.next_node = self.head
			nd.prev_node = None
			self.head.prev_node = nd
			self.head = nd

	def insert_at_end(self, item):
		"""Insert an item at the end of the list."""
		nd = Node(item)
		if self.head is None:
			self.head = nd
		else:
			current = self.head
			while current.next_node is not None:
				current = current.next_node

			nd.prev_node = current
			current.next_node = nd

	def insert_after_node(self, key, item):
		"""Insert an item after key."""
		pass

	def insert_before_node(self, key, item):
		"""Insert an item before key."""
		pass

	def remove(self, item):
		"""Remove an item."""
		if self.head is None or self.head.data == item:
			self.head = None
		elif self.head is not None:
			current = self.head
			while current.data != item:
				current = current.next_node

			tmp = current.next_node
			current.data = tmp.data
			current.next_node = tmp.next_node

	def display(self):
		"""Display the items."""
		if self.head is None:
			print "Doubly linked list is empty."
		else:
			current = self.head
			while current is not None:
				print "%d " % current.data,
				current = current.next_node

	def reverse(self):
		"""Reverse the doubly linked list."""
		if self.head is not None:
			front_node = self.head
			current = self.head

			while current.next_node is not None:
				current = current.next_node
			
			rear_node = current


if __name__ == '__main__':
	dll = DoublyLinkedList()
	for x in xrange(10):
		dll.insert_at_front(x)

	dll.display()
	