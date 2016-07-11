# Python implementation of various searching algorithms.

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
