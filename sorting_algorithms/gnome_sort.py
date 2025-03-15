"""
Gnome sort algorithm module
"""


class GnomeSort:
    def __init__(self):
        pass

    def gnome(self, aList):
        nlist = list(aList)
        size = len(nlist)

        if size < 2:
            return nlist

        pivot = 0
        nlist_length = len(nlist)
        while pivot < nlist_length - 1:
            if nlist[pivot] > nlist[pivot + 1]:
                nlist[pivot + 1], nlist[pivot] = nlist[pivot], nlist[pivot + 1]
                if pivot > 0:
                    pivot -= 2
            pivot += 1

        return nlist

    def sort(self, arr):
        return self.gnome(arr)
