"""
Module for quick sort algorithm.
"""


class StringQuickSort:
    def __init__(self):
        pass

    def sort(self, arr):
        """Sort an array of strings using QuickSort with optimizations for large arrays"""
        if not arr:
            return []

        # Use iterative approach to avoid recursion depth issues
        self._quick_sort_iterative(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort_iterative(self, arr, low, high):
        """Non-recursive QuickSort implementation using a stack"""
        # Create an auxiliary stack
        size = high - low + 1
        stack = [0] * size

        # Initialize top of stack
        top = -1

        # Push initial values to stack
        top += 1
        stack[top] = low
        top += 1
        stack[top] = high

        # Keep popping from stack while it's not empty
        while top >= 0:
            # Pop high and low
            high = stack[top]
            top -= 1
            low = stack[top]
            top -= 1

            # Partition the array
            p = self._partition(arr, low, high)

            # If there are elements on the left side of pivot,
            # push left side to stack
            if p - 1 > low:
                top += 1
                stack[top] = low
                top += 1
                stack[top] = p - 1

            # If there are elements on the right side of pivot,
            # push right side to stack
            if p + 1 < high:
                top += 1
                stack[top] = p + 1
                top += 1
                stack[top] = high

    def _partition(self, arr, low, high):
        """Improved partition function with median-of-three pivot selection"""
        # Choose better pivot using median-of-three
        mid = (low + high) // 2

        # Sort low, mid, high elements
        if arr[mid] < arr[low]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[high] < arr[low]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[high] < arr[mid]:
            arr[mid], arr[high] = arr[high], arr[mid]

        # Place pivot at position high-1
        pivot_index = mid
        pivot = arr[pivot_index]

        # Index of smaller element
        i = low

        # Traverse through all elements
        for j in range(low, high + 1):
            if j == pivot_index:
                continue

            # If current element is smaller than pivot
            if arr[j] <= pivot:
                # Swap if i and j are different
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]

                # Move to next potential swap position if we didn't just
                # swap with the pivot
                if i != pivot_index:
                    i += 1

        # Put pivot in its final place
        arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        return i
