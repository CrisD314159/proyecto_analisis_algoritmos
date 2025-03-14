"""
Gnome sort algorithm module
"""


class GnomeSort:
    def __init__(self):
        pass

    def gnome(self, arr, n):
        index = 0
        while index < n:
            if index == 0:
                index = index + 1
            if arr[index] >= arr[index - 1]:
                index = index + 1
            else:
                arr[index], arr[index-1] = arr[index-1], arr[index]
                index = index - 1

        return arr

    def sort(self, arr):
        return self.gnome(arr, len(arr))
