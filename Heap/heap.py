# Python implementation of a Min heap.

class Heap(object):
	def __init__(self, capacity=0):
		self._arr = []
		self.capacity = capacity
		self.size = 0

	def parent(self, index):
		return (index-1)/2


	def left(self, index):
		return (2*index + 1)


	def right(self, index):
		return (2*index + 2)

	
	def insert(self, key):
		"""Insert an element into the heap."""
		if self.size == self.capacity:
			print "Heap is full."
			return
		else:
			# Insert the element at the end of the list.
			self._arr.append(key)
			self.size += 1
			index = len(self._arr)-1

			# Compare the key with it's parent recursively.
			while index != 0 and self._arr[self.parent(index)] > self._arr[index]:
				self._arr[index], self._arr[self.parent(index)] = self._arr[self.parent(index)], self._arr[index]
				index = self.parent(index)


	def delete(self, key):
		pass


	def extract_min(self):
		"""Remove the minimum element from the heap."""
		if self.size == 0:
			print "Heap is empty."
			return
		elif self.size == 1:
			min_element = self._arr[0]
			self.size -= 1
			return min_element
		else:
			min_element = self._arr[0]
			self._arr[0] = self._arr[self.size-1]
			self.size -= 1
			self.heapify(0)

			return min_element

	def heapify(self, index):
		left = self.left(index);
		right = self.right(index);
		smallest = index;

		if left < self.size and self._arr[left] < self._arr[smallest]:
			smallest = left;
		elif right < self.size and self._arr[right] < self._arr[smallest]:
			smallest = right

		if smallest != index:
			self._arr[index], self._arr[smallest] = self._arr[smallest], self._arr[index]
			self.heapify(smallest)


	def get_min(self):
		return self._arr[0]

	def size(self):
		return self.size

