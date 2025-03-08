"""
Module for quick sort algorithm.
"""


class QuickSort:
    """
    Class for quick Sort algorithm.
    """

    def __init__(self):
        pass

    def quick_sort(self, arr):
        """
        Quick Sort algorithm implementation.
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def run_selection_sort(self, arr):
        """
        Run method for Selection Sort algorithm.
        """
        self.quick_sort(arr)
