# Common sorting algorithms implemented in Python.

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
            for j in xrange(i, self.arr_size):
                if self.arr[i] > self.arr[j]:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

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
            for j in xrange(i, self.arr_size):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

        return self.arr


    def merge_sort(self):
        """
        Time Complexity: O(nlogn)
        """
        pass


    def partition(self, low, high):
        """Return a pivot element for Quicksort."""
        key = self.arr[high]
        pivot = low
        for i in xrange(low, high):
            if self.arr[i] <= key:
                self.arr[i], self.arr[pivot] = self.arr[pivot], self.arr[i]
                pivot += 1

        self.arr[pivot], self.arr[high] = self.arr[high], self.arr[pivot]
        return pivot


    def quick_sort_inplace(self, low, high):
        """
        Time Complexity: O(nlogn)
        Space Complexity: O(1)
        """
        if low < high:
            pivot = self.partition(low, high)
            self.quick_sort_inplace(low, pivot-1)
            self.quick_sort_inplace(pivot+1, high)


    def quick_sort_space(self, data):
        """
        Quick sort.

        * Easy to understand.
        * Consumes more space.
        * Less efficient.
        """
        if len(data) > 1:
            less = []
            equal = []
            greater = []
            pivot = data[0]

            for x in data:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                else:
                    greater.append(x)

            return self.quick_sort_space(less) + equal + self.quick_sort_space(greater)

        else:
            return data

    def heap_sort(self):
        """
        Time Complexity: O(nlogn)
        """
        pass


    def display(self):
        """Print the elements of the array."""
        print self.arr
