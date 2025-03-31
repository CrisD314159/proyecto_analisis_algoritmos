"""
Module for quick sort algorithm.

Explicación:
QuickSort es uno de los algoritmos de ordenamiento más eficientes y más utilizados
Básicamente lo que el algoritmo hace es seleccionar un elemento como pivote y y particionar la lista
por los elementos menores y mayores que el pivote. Luego para cada lista estructurada, se le aplica
otra vez al algoritmo de forma recursiva hasta que se llegue al caso base, que es cuando la lista tiene
dos elementos o menos

Precauciones:
La mayoria de los casos el algoritmo resulta eficiente, pero dependiendo de la elección del pivote
puede incluso resultar en una ineficiencia

O(n log n) pero O(n^2) en el peor de los casos (mala elección de pivotes)
"""


class StringQuickSort:
    def __init__(self):
        pass

    def quick_sort(self, arr):
        """
        Quick Sort algorithm implementation.
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def run_quick_sort(self, arr):
        """
        Run method for Selection Sort algorithm.
        """
        return self.quick_sort(arr)
