"""
Radix sort algorithm implementation as a class.
"""


from collections import defaultdict


class RadixSort:
    def __init__(self, arr):
        self.arr = arr
        self.max_length = max(len(word) for word in arr) if arr else 0

    def sort(self):
        for pos in range(self.max_length - 1, -1, -1):
            self.arr = self._counting_sort(self.arr, pos)
        return self.arr

    def _counting_sort(self, arr, pos):
        buckets = defaultdict(list)

        for word in arr:
            char = word[pos] if pos < len(word) else ""
            buckets[char].append(word)

        sorted_arr = []
        for key in sorted(buckets.keys()):  # Sorting keys ensures lexicographic order
            sorted_arr.extend(buckets[key])

        return sorted_arr
