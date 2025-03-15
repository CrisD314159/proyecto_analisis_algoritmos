"""
Module for heap sort algorithm.

Explicación
Este algoritmo utiliza una estructura de datos llamada heap, es en sintesis es un arbol binario
Para este caso, se usa max heap, donde el nodo padre es mayor que los nodos hijos
El algoritmo inicia creando un heap con los elementos del array, luego se intercambia el primer
elemento con el último, y se llama recursivamente a heapify para que el array quede ordenado
de mayor a menor de forma descendente

Precauciones:
El algoritmo generalmente es eficiente para listas grandes

Puede fallar si se desbalancea el heap, ya que 
en todo momento se espera que el nodo padre sea el mayor

O(n log n)
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
