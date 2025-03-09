"""
Bitonic sort module
"""


class BitonicSort:
    """
    A class that implements the Bitonic Sort algorithm.
    """

    @staticmethod
    def compare_and_swap(arr, i, j, ascending):
        """
        Compare and swap method for bitonic sort algorithm.
        """
        if (ascending and arr[i] > arr[j]) or (not ascending and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def bitonic_merge(arr, low, cnt, ascending):
        """
        Bitonic merge method for bitonic sort algorithm.
        """
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                BitonicSort.compare_and_swap(arr, i, i + k, ascending)
            BitonicSort.bitonic_merge(arr, low, k, ascending)
            BitonicSort.bitonic_merge(arr, low + k, k, ascending)

    @staticmethod
    def bitonic_sort_recursive(arr, low, cnt, ascending):
        """
        Bitonic sort recursive method for bitonic sort algorithm.
        """
        if cnt > 1:
            k = cnt // 2
            BitonicSort.bitonic_sort_recursive(arr, low, k, True)
            BitonicSort.bitonic_sort_recursive(arr, low + k, k, False)
            BitonicSort.bitonic_merge(arr, low, cnt, ascending)

    @staticmethod
    def sort(arr):
        """
        Bitonic sort algorithm implementation.
        """
        n = len(arr)
        BitonicSort.bitonic_sort_recursive(arr, 0, n, True)
