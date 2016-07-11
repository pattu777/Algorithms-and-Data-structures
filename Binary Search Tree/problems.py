import Queue

from bst import BinarySearchTree, Node

def is_identical(tr1, tr2):
		"""Check if two trees are identical or not."""
		if tr1 is None and tr2 is None:
			return True

		if tr1 is not None and tr2 is not None:
			return tr1.data == tr2.data and is_identical(tr1.left, tr2.left) and is_identical(tr1.right, tr2.right) 

		return False

def level_order_traversal(tr):
	"""Perform BFS or level-order traversal of the tree."""
	if tr.get_root() is None:
		print "Tree is empty."
	else:
		my_q = Queue.Queue()
		nd = tr.get_root()

		# Insert the root element into the Queue.
		my_q.put(nd)
		while not my_q.empty():
			current = my_q.get()
			print "%d " % current.data,
			if current.left is not None:
				my_q.put(current.left)
			if current.right is not None:
				my_q.put(current.right)