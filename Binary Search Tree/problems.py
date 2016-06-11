from bst import BinarySearchTree, Node

def is_identical(tr1, tr2):
		"""Check if two trees are identical or not."""
		if tr1 is None and tr2 is None:
			return True

		if tr1 is not None and tr2 is not None:
			return tr1.data == tr2.data and is_identical(tr1.left, tr2.left) and is_identical(tr1.right, tr2.right) 

		return False
