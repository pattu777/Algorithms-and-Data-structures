import unittest

from search import SearchingAlgos

class SearchingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SearchingTest, self).__init__(*args, **kwargs)
        self.test_arr = [x for x in xrange(100)]

    def test_linear_search(self):
        """Unit tests for liner search."""
        var = SearchingAlgos(arr=self.test_arr)
        self.assertTrue(var.linear_search(50))
        self.assertFalse(var.linear_search(181))
        self.assertFalse(var.iterative_binary_search(-1231))
        self.assertTrue(var.iterative_binary_search(79))

    def test_iterative_binary_search(self):
        """Unit test for iterative binary search."""
        var = SearchingAlgos(arr=self.test_arr)
        self.assertTrue(var.iterative_binary_search(50))
        self.assertFalse(var.iterative_binary_search(181))
        self.assertFalse(var.iterative_binary_search(-1231))
        self.assertTrue(var.iterative_binary_search(79))

    def test_recursive_binary_search(self):
        """Unit tests for recursive binary search."""
        var = SearchingAlgos(arr=self.test_arr)
        self.assertTrue(var.recursive_binary_search(0, len(self.test_arr)-1, 50))
        self.assertFalse(var.recursive_binary_search(0, len(self.test_arr)-1, 181))
        self.assertFalse(var.recursive_binary_search(0, len(self.test_arr)-1, -1231))
        self.assertTrue(var.recursive_binary_search(0, len(self.test_arr)-1, 79))


if __name__ == '__main__':
    unittest.main()
