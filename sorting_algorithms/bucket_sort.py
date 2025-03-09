"""
Module for bucket sort algorithm.
"""
from collections import defaultdict


class BucketSort:
    """
    Class for Selection Sort algorithm.
    """

    @staticmethod
    def bucket_sort(arr):
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
