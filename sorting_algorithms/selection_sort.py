"""
Module for selection sort algorithm.
"""


class SelectionSort:
    """
    Class for Selection Sort algorithm.
    """
    @staticmethod
    def selection_sort(arr):
        """
        Method for Selection Sort algorithm.
        """
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
