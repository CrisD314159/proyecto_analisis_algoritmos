"""
Gnome sort algorithm module

Explicación:
Gnome sort es un algoritmo lento pero simple de ordenamiento, que como selection sort
recorre la lista de izquierda a derecha
Este elgoritmo empieza por el primer elemento, acto seguido lo compara con el
sigiente, si el primero es menor que el segundo, sigue en su iteración

En caso de que el primer elemento sea mayor que el segundo, los intercambia y retrocede
una posición, repitiendo el proceso hasta que el primer elemento sea menor que el segundo
y pueda entregar una lista ordenada

Precauciones:
El algoritmo es ineficiente para listas grandes

En algunos casos puede ser más eficiente que otros algoritmos de ordenamiento si la 
lista está casi ordenada

O(n) en su mejor caso, O(n^2) en su peor caso
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
