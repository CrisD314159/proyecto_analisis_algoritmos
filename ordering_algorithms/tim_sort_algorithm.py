"""
This module contains the implementation of the Tim Sort algorithm.
"""


class TimSort:
    """
      This class contains the implementation of the Tim Sort algorithm.
    """

    def __init__(self):
        self.MIN_MERGE = 32

    def insertion_sort(self, arr, left, right):
        """
        Insertion method for the Tim Sort algorithm.
        """
        for i in range(left + 1, right + 1):
            temp = arr[i]
            j = i - 1
            while j >= left and arr[j] > temp:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp

    def merge(self, arr, l, m, r):
        """
        Merge method for the Tim Sort algorithm.
        """
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]

        i, j, k = 0, 0, l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def tim_sort(self, arr):
        """
        Tim Sort algorithm implementation
        """
        n = len(arr)
        for i in range(0, n, self.MIN_MERGE):
            self.insertion_sort(arr, i, min((i + self.MIN_MERGE - 1), (n - 1)))

        size = self.MIN_MERGE
        while size < n:
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min((left + 2 * size - 1), (n - 1))
                if mid < right:
                    self.merge(arr, left, mid, right)
            size *= 2

    def run_tim_sort(self, arr):
        """
        Executes the Tim Sort algorithm on the provided array.
        """
        self.tim_sort(arr)
