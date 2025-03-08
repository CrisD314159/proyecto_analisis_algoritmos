"""
Module for selection sort algorithm.
"""


class SelectionSort:
    """
    Class for Selection Sort algorithm.
    """

    def __init__(self):
        pass

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def run_selection_sort(self, arr):
        """
        Run method for Selection Sort algorithm.
        """
        self.selection_sort(arr)
