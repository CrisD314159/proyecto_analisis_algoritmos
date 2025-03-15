"""
Radix sort algorithm implementation as a class.
Explicación:
Este algoritmo resulta interesante que que no compara los elementos del array, sino que los ordena
los elementos caracter a caracter en este caso.

El algoritmo inicia en la ultima posición de los elementos (ultima letra)
y al inicio crea un diccionario (buckets) con los elementos de la lista, donde la llave es el
ultimo caracter:

Para ordenar ["apple", "banana", "kiwi"]:
“e” → ["apple"]
“a” → ["banana"]
“i” → ["kiwi"]

y así sucesivamente con los demás caracteres, hasta que la lista esté ordenada

Precauciones:
El algoritmo es eficiente para listas de strings, pero si estas listas
son muy grandes y las palabras tienen demasiados caracteres, el algoritmo
se vuelve inneficiente

O(n * k) donde k es el número de caracteres de la palabra más larga



"""


from collections import defaultdict


class RadixSort:
    def __init__(self, arr):
        self.arr = arr
        self.max_length = max(len(word) for word in arr) if arr else 0

    def sort(self):
        for pos in range(self.max_length - 1, -1, -1):
            self.arr = self._counting_sort(self.arr, pos)
        return self.arr

    def _counting_sort(self, arr, pos):
        buckets = defaultdict(list)

        for word in arr:
            char = word[pos] if pos < len(word) else ""
            buckets[char].append(word)

        sorted_arr = []
        for key in sorted(buckets.keys()):  # Sorting keys ensures lexicographic order
            sorted_arr.extend(buckets[key])

        return sorted_arr
