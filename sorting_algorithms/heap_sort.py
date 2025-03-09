"""
Module for heap sort algorithm.
"""


class HeapSort:
    """
    Class for heap Sort algorithm.
    """
    @staticmethod
    def heapify(arr, n, i):
        """
        Heapify method for heap Sort algorithm.
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            HeapSort.heapify(arr, n, largest)

    @staticmethod
    def heap_sort(arr):
        """
        Heap Sort algorithm implementation.
        """
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            HeapSort.heapify(arr, i, 0)
