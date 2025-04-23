"""
Module for merge sort
"""


class MergeSort:
    """
    A class that implements the merge sort algorithm.
    Supports sorting both numeric and string arrays.
    """

    def __init__(self):
        """Initialize the MergeSort class."""
        pass

    def sort(self, arr):
        """
        Sort an array using the merge sort algorithm.

        Args:
            arr: The array to be sorted (can contain numbers or strings)

        Returns:
            A new sorted array
        """
        return self._merge_sort(arr)

    def _merge_sort(self, arr):
        """
        Internal recursive merge sort implementation.

        Args:
            arr: The array to be sorted

        Returns:
            A new sorted array
        """
        # Base case: arrays with 0 or 1 element are already sorted
        if len(arr) <= 1:
            return arr

        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        left_half = self._merge_sort(left_half)
        right_half = self._merge_sort(right_half)

        # Merge the sorted halves
        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        """
        Merge two sorted arrays into a single sorted array.

        Args:
            left: The left sorted array
            right: The right sorted array

        Returns:
            A merged sorted array
        """
        result = []
        i = j = 0

        # Compare elements from both arrays and add the smaller one to the result
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add any remaining elements from the left array
        while i < len(left):
            result.append(left[i])
            i += 1

        # Add any remaining elements from the right array
        while j < len(right):
            result.append(right[j])
            j += 1

        return result

#
