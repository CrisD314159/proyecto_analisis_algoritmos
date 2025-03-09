"""
Module for pingeon sort algorithm.
"""


class PingeonSort:
    """
    Class for pingeon Sort algorithm.
    """
    @staticmethod
    def pigeonhole_sort(arr):
        """
        Pingeon Sort algorithm implementation.
        """
        if not arr:
            return []

        min_value = min(arr)
        max_value = max(arr)
        size = ord(max_value[0]) - ord(min_value[0]) + 1

        holes = [[] for _ in range(size)]

        for word in arr:
            index = ord(word[0]) - ord(min_value[0])
            holes[index].append(word)

        index = 0
        for hole in holes:
            for word in sorted(hole):
                arr[index] = word
                index += 1
