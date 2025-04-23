"""
Module for Radix nodes
"""
from collections import defaultdict


class NodoCadena:
    def __init__(self, valor=""):
        self.valor = valor
        self.siguiente = None


class ColaEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamano = 0

    def encolar(self, cadena):
        self.tamano += 1
        temp = NodoCadena(cadena)
        if self.inicio is None:
            self.inicio = temp
            self.fin = temp
        else:
            self.fin.siguiente = temp
            self.fin = temp

    def decolar(self):
        if self.esta_vacia():
            return None
        self.tamano -= 1
        valor = self.inicio.valor
        self.inicio = self.inicio.siguiente
        return valor

    def esta_vacia(self):
        return self.tamano == 0


class RadixSortNodes:
    def sort(self, arr):
        if not arr:
            return arr

        max_len = max(len(s) for s in arr)
        arr = [s.ljust(max_len) for s in arr]

        for i in reversed(range(max_len)):
            buckets = defaultdict(ColaEnlazada)
            for s in arr:
                index = ord(s[i])
                buckets[index].encolar(s)

            arr = []
            for key in sorted(buckets):  # Keep order consistent
                queue = buckets[key]
                while not queue.esta_vacia():
                    arr.append(queue.decolar())

        return [s.rstrip() for s in arr]
