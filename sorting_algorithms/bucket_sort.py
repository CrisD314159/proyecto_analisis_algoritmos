"""
Module for bucket sort algorithm.
"""


class BucketSort:
    def __init__(self, bucket_size=5):
        """
        Initialize BucketSort with specified bucket size

        Args:
            bucket_size (int): Number of buckets to use
        """
        self.bucket_size = bucket_size

    def sort(self, arr):
        """
        Sort an array using Bucket Sort algorithm

        Args:
            arr (list): List to be sorted

        Returns:
            list: Sorted list
        """
        if not arr:
            return []

        # For strings, we'll use the first character's ASCII value to determine buckets
        # Handle empty strings by placing them in the first bucket

        # Find min and max values for bucket range calculation
        min_val = min(arr, key=lambda x: ord(x[0]) if x else 0) if arr else ""
        max_val = max(arr, key=lambda x: ord(x[0]) if x else 0) if arr else ""

        min_ascii = ord(min_val[0]) if min_val else 0
        max_ascii = ord(max_val[0]) if max_val else 0

        # Create buckets
        bucket_count = self.bucket_size
        buckets = [[] for _ in range(bucket_count)]

        # Distribute elements into buckets
        for item in arr:
            if not item:  # Handle empty strings
                buckets[0].append(item)
            else:
                # Calculate which bucket the item should go into
                ascii_val = ord(item[0])
                # Ensure the last bucket includes the maximum value
                bucket_index = min(
                    int((ascii_val - min_ascii) * bucket_count /
                        (max_ascii - min_ascii + 1)),
                    bucket_count - 1
                )
                buckets[bucket_index].append(item)

        # Sort individual buckets using insertion sort
        for i in range(bucket_count):
            self._insertion_sort(buckets[i])

        # Concatenate buckets back into a single array
        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result

    def _insertion_sort(self, arr):
        """
        Insertion sort for sorting individual buckets

        Args:
            arr (list): List to be sorted
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
