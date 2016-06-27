# Sorting algorithms implemented in Python.

import unittest

class SortingAlgos(object):
    def __init__(self, arr=None):
        self.arr = arr
        self.arr_size = len(self.arr)


    def bubble_sort(self):
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in xrange(self.arr_size):
            for j in xrange(self.arr_size-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

        return self.arr


    def insertion_sort(self):
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in xrange(1, self.arr_size):
            key = self.arr[i]
            j = i-1
            while j >= 0 and key < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key

        return self.arr


    def selection_sort(self):
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in xrange(self.arr_size):
            min_index = i
            for j in xrange(i+1, self.arr_size):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

        return self.arr


    def merge_sort(self):
        """
        Time Complexity: O(nlogn)
        """
        pass


    def partition(self):
        """Return a pivot element for Quicksort."""
        pass


    def quick_sort(self, low, high):
        """
        Time Complexity: O(nlogn)
        """
        if low < high:
            pivot = self.partition(low, high)
            self.quick_sort(low, pivot-1)
            self.quick_sort(pivot+1, high)


    def heap_sort(self):
        """
        Time Complexity: O(nlogn)
        """
        pass


    def display(self):
        """Print the elements of the array."""
        print self.arr


class SortingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SortingTest, self).__init__(*args, **kwargs)
        self.test_arr = [[], [1], [1, 2], [2, 1], [5, 2, 7, 1, 8], [1, 2, 5, 7, 8],
                [10, 272, 100, -98, 876, 877754, 98124, 0, 1000000, -100]]


    def test_bubble_sort(self):
        """Test bubble sort."""
        for arr in self.test_arr:
            sort = SortingAlgos(arr=arr)
            reversed_arr = sort.bubble_sort()
            self.assertEqual(sorted(arr), reversed_arr)


    def test_selection_sort(self):
        for arr in self.test_arr:
            sort = SortingAlgos(arr=arr)
            reversed_arr = sort.selection_sort()
            self.assertEqual(sorted(arr), reversed_arr)



    def test_insertion_sort(self):
        for arr in self.test_arr:
            sort = SortingAlgos(arr=arr)
            reversed_arr = sort.insertion_sort()
            self.assertEqual(sorted(arr), reversed_arr)


    def test_quick_sort(self):
        for arr in self.test_arr:
            sort = SortingAlgos(arr=arr)
            reversed_arr = sort.quick_sort()
            self.assertEqual(sorted(arr), reversed_arr)

    """
    def test_merge_sort(self):
        for arr in self.test_arr:
            sort = SortingAlgos(arr=arr)
            reversed_arr = sort.merge_sort()
            self.assertEqual(sorted(arr), reversed_arr)



    def test_heap_sort(self):
        for arr in self.test_arr:
            sort = SortingAlgos(arr=arr)
            reversed_arr = sort.heap_sort()
            self.assertEqual(sorted(arr), reversed_arr)


    """
if __name__ == '__main__':
    unittest.main()

