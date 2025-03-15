"""
Module for selection sort algorithm.

Explicación:
Selection sort es uno de los algoritmos más ineficientes pero simples de ordenamiento
Básicamente lo que el algoritmo hace es recorrer elemento por elemento de la lista, 
buscando el menor elemento, una vez encontrado, lo intercambia con el primer elemento
y así sucesivamente hasta que la lista esté ordenada

Precauciones:
Si es una lista pequeña, puede ser eficiente, de lo contrario, es muy ineficiente

O(n^2)
"""


class SelectionSort:
    """
    Class for Selection Sort algorithm.
    """
    @staticmethod
    def selection_sort(arr):
        """
        Method for Selection Sort algorithm.
        """
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
