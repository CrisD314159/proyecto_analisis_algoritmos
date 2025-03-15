"""
Module for comb sort algorithm.

Explicación:
Este algoritmo es una mejora del bubble sort, pero con comparaciones reducidas

el algoritmo inicia con un gap, que es el espacio entre los elementos a comparar
también elige un shrink, que es el factor de reducción del gap

El algoritmo realiza una iteración para comparar el elemento del indice i con 
el elemento del indice i mas el gap, acto seguido reduce el gap y repite el proceso

Cuando el gap es 1, el algortimo se da por hecho que la lista está ordenada y termina
la iteración

Precauciones:

en el mejor de los casos es O(n log n), pero en el peor de los casos es O(n^2)
"""


class CombSort:
    """
    Class for Comb Sort algorithm.
    """

    @staticmethod
    def comb_sort(arr):
        """
        Comb Sort algorithm implementation.
        """
        gap = len(arr)
        shrink = 1.3
        sorted_list = False

        while not sorted_list:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted_list = True

            i = 0
            while i + gap < len(arr):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted_list = False
                i += 1
