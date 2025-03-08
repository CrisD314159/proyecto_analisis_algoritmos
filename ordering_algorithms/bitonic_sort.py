"""
Bitonic sort module
"""


def compare_and_swap(arr, i, j, ascending):
    """
    Compare and swap method for bitonic sort algorithm.
    """
    if (ascending and arr[i] > arr[j]) or (not ascending and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]


def bitonic_merge(arr, low, cnt, ascending):
    """
    Bitonic merge method for bitonic sort algorithm.
    """
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compare_and_swap(arr, i, i + k, ascending)
        bitonic_merge(arr, low, k, ascending)
        bitonic_merge(arr, low + k, k, ascending)


def bitonic_sort_recursive(arr, low, cnt, ascending):
    """
    Bitonic sort recursive method for bitonic sort algorithm.
    """
    if cnt > 1:
        k = cnt // 2
        bitonic_sort_recursive(arr, low, k, True)
        bitonic_sort_recursive(arr, low + k, k, False)
        bitonic_merge(arr, low, cnt, ascending)


def bitonic_sort(arr):
    """
    Bitonic sort algorithm implementation.
    """
    n = len(arr)
    bitonic_sort_recursive(arr, 0, n, True)
