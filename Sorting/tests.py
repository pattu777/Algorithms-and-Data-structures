import unittest

from sort import SortingAlgos

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


    def test_quick_sort_inplace(self):
        for arr in self.test_arr:
            sort = SortingAlgos(arr=arr)

            sort.quick_sort_inplace(0, len(arr)-1)
            self.assertEqual(sorted(arr), sort.arr)

            reversed_arr = sort.quick_sort_space(arr)
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

