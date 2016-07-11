# Unit tests for hash table.

import unittest

from hashtable import HashTable

class HashTableTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(HashTableTest, self).__init__(*args, **kwargs)
		self.my_map = HashTable(10)
		
	def test_hashmap(self):
		self.my_map.put(1, "A")
		self.assertEqual(self.my_map.get(1), "A")
		self.assertFalse(self.my_map.get(1) == "BABA")
		self.assertEqual(self.my_map.get(211), None)

		self.my_map.put(2, "Hello World")
		self.assertEqual(self.my_map.get(2), "Hello World")
		
		self.my_map.remove(2)
		self.assertFalse(self.my_map.get(2) == "Hello World")

if __name__ == '__main__':
	unittest.main()