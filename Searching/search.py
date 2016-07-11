# Python implementation of various searching algorithms.

import unittest

class SearchingAlgos(object):
    def __init__(self, arr):
        self.arr = arr

    def linear_search(self, var):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.arr is None or len(self.arr) == 0:
            return False
        else:
            for x in self.arr:
                if x == var:
                    return True
            return False

    def iterative_binary_search(self, var):
        """
        Time Complexity: O(nlogn)
        Space Complexity: O(1)
        """
        if self.arr is None or len(self.arr) == 0:
            return False
        else:
            low = 0
            high = len(self.arr)-1
            while low < high:
                mid = low + (high-low)/2
                if var < self.arr[mid]:
                    high = mid
                elif var > self.arr[mid]:
                    low = mid+1
                else:
                    return True
            return False

    def recursive_binary_search(self, low, high, var):
        """
        Time Complexity - O(n logn)
        Space Complexity - O(1)
        """
        mid = low + (high-low)/2
        if low > high:
            return False
        elif var < self.arr[mid]:
            self.recursive_binary_search(low, mid-1, var)
        elif var > self.arr[mid]:
            self.recursive_binary_search(mid+1, high, var)
        else:
            return True
        

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
