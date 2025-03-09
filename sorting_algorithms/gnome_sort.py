"""
Gnome sort algorithm module
"""


class GnomeSort:
    """
    A class that implements the Gnome Sort algorithm.
    """

    @staticmethod
    def gnome_sort(arr):
        """
        Gnome sort algorithm implementation.
        """
        index = 0
        n = len(arr)
        while index < n:
            if index == 0 or arr[index] >= arr[index - 1]:
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index -= 1
