"""
Module for quick sort algorithm.
"""


class QuickSort:
    """
    Class for quick Sort algorithm.
    """

    @staticmethod
    def quick_sort(arr):
        """
        Quick Sort algorithm implementation.
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return QuickSort.quick_sort(left) + middle + QuickSort.quick_sort(right)
