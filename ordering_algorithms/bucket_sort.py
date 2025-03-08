"""
Module for bucket sort algorithm.
"""
from collections import defaultdict


class BucketSort:
    """
    Class for Selection Sort algorithm.
    """

    def __init__(self):
        pass

    def bucket_sort(self, arr):
        """
          Bucket sort algorithm implementation.
        """
        if not arr:
            return []

        buckets = defaultdict(list)

        for word in arr:
            first_letter = word[0].lower()
            buckets[first_letter].append(word)

        sorted_arr = []
        for key in sorted(buckets.keys()):
            sorted_arr.extend(sorted(buckets[key]))

        arr[:] = sorted_arr  # Copy back sorted elements

    def run_selection_sort(self, arr):
        """
        Run method for Selection Sort algorithm.
        """
        self.bucket_sort(arr)
