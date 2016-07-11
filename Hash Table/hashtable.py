# An array based implementation of a hash table.

class Item(object):
	def __init__(self, key=None, value=None):
		self.key = key
		self.value = value

class HashTable(object):
	def __init__(self, size=10):
		self.size = size
		self.arr = [[] for _ in xrange(self.size)]
		
	def hash_function(self, key):
		"""Compute a hash function for the given key."""
		return key % self.size

	def put(self, key, value):
		"""Insert a key, value pair into the hash table."""
		item = Item(key, value)
		hash_index = self.hash_function(key)
		for x in self.arr[hash_index]:
			if x == key:
				x.value = value
				return
		self.arr[hash_index].append(item)

	def get(self, key):
		"""Retrieve a value for a given key from the hash table."""
		hash_index = self.hash_function(key)
		for x in self.arr[hash_index]:
			if x.key == key:
				return x.value
		return None

	def remove(self, key):
		"""Remove a key, value pair from the map."""
		hash_index = self.hash_function(key)
		if len(self.arr[hash_index]) != 0:
			for i, x in enumerate(self.arr[hash_index]):
				if x.key == key:
					self.arr[hash_index].pop(i)
					return
