"""
Module for pingeon sort algorithm.

Explicación
Tabién y como radix sort, pingeon sort es un algoritmo de ordenamiento no comparativo
En principio, el algoritmo separa las palabras más pequeñas y más grandes de la lista
Luego toma el primer caracter de la palabra mas pequeña y el primer caracter de la más grande

Acto seguido compara la distancias de los caracteres y en base a eso crea los huecos (holes)
por ejemplo

Minima = "apple"
Maxima = "kiwi"
distancia = a - k = 10  + 1 =  => por lo tanto pingeonhole crea 11 huecos para ordenar la lista

Luego, para cada palabra encuentra el íncide del casillero o hueco mediante el siguiente calculo
index = ord(word[0]) - ord(min_value[0]) 
Que es la distancia de la primera letra de la palabra, con la primera letra de la palabra más 

Una vez encuentra el índice, inserta la palabra en el casillero correspondiente

finalmente, itera sobre la lista de casilleros y ordena las palabras en cada casillero
y las inserta en la lista original

Precauciones:
Se puede volver ineficiente si las palabras son muy largas y la distancia entre caracteres 
es muy grande ya que tiene que crear muchos casilleros y recorrer la lista muchas veces

Si la distancia entre las palabras es muy pequeña (pocos casilleros) puede ser muy eficiente

O(n + k) donde k es el numero de casilleros o huecos



"""


class PingeonSort:
    """
    Class for pingeon Sort algorithm.
    """
    @staticmethod
    def pigeonhole_sort(arr):
        """
        Pingeon Sort algorithm implementation.
        """
        if not arr:
            return []

        min_value = min(arr)
        max_value = max(arr)
        size = ord(max_value[0]) - ord(min_value[0]) + 1

        holes = [[] for _ in range(size)]

        for word in arr:
            index = ord(word[0]) - ord(min_value[0])
            holes[index].append(word)

        index = 0
        for hole in holes:
            for word in sorted(hole):
                arr[index] = word
                index += 1
