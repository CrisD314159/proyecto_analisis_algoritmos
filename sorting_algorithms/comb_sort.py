"""
Module for comb sort algorithm.
"""


class CombSort:
    """
    Class for Comb Sort algorithm.
    """

    @staticmethod
    def comb_sort(arr):
        """
        Comb Sort algorithm implementation.
        """
        gap = len(arr)
        shrink = 1.3
        sorted_list = False

        while not sorted_list:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted_list = True

            i = 0
            while i + gap < len(arr):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted_list = False
                i += 1
