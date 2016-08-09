import unittest

from heap import Heap

class HeapTest(unittest.TestCase):
	def heap_test(self):
		h = Heap(11)
		h.insert(3)
		h.insert(2)
		#h.delete(1)
		h.insert(15)
		h.insert(5)
		h.insert(4)
		h.insert(45)

		print h.extract_min()
		print h.get_min()

		#h.decreaseKey(2, 1)
		print h.get_min()


if __name__ == '__main__':
	h = Heap(11)
	h.insert(3)
	h.insert(2)
	#h.delete(1)
	h.insert(15)
	h.insert(5)
	h.insert(4)
	h.insert(45)

	print h.extract_min()
	print h.get_min()

	#h.decreaseKey(2, 1)
	print h.get_min()
