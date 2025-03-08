"""
Radix sort algorithm implementation as a class.
"""

from collections import defaultdict


class RadixSort:
    """
    A class that implements the radix sort algorithm for sorting strings.
    """

    def __init__(self):
        """
        Initialize the RadixSort object.
        """
        pass

    def _counting_sort(self, arr, pos):
        """
        Counting sort algorithm implementation used as a helper method.

        Args:
            arr: List of strings to sort
            pos: Position of character to sort by
        """
        buckets = defaultdict(list)
        for word in arr:
            char = word[pos] if pos < len(word) else ""
            buckets[char].append(word)

        index = 0
        for key in sorted(buckets.keys()):
            for word in buckets[key]:
                arr[index] = word
                index += 1

    def sort(self, arr):
        """
        Sort the given array using radix sort algorithm.

        Args:
            arr: List of strings to sort

        Returns:
            The sorted list (same object, sorted in-place)
        """
        if not arr:
            return arr

        max_length = max(len(word) for word in arr)
        for pos in range(max_length - 1, -1, -1):
            self._counting_sort(arr, pos)

        return arr
