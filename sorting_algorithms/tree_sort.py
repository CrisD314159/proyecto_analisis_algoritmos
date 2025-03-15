"""
Tree sort module

Explicación del algoritmo:
Este utiliza un arbol de búsqueda binaria para ordenar los elementos del array
como primeta instancia, crea un nodo raiz con el primer elemento del array, luego
ordena en un arbol binario los elementos restantes, si el elemento es menor que el nodo
actual, se inserta en la izquierda, si es mayor en la derecha, luego se realiza un recorrido 
inorder (izquierda, nodo, derecha) para obtener el array ordenado

Precauciones:
El algoritmo con listas muy grandes puede ser inestable y lento, ya que el arbol
puede llegar a ser muy profundo, lo que puede causar un stack overflow o un desbalance en el arbol

O(n log n) pero O(n^2) si el arbol es mas profundo
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        # Insert to the left if key is less; otherwise, to the right
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)

    def inorder(self):
        # In-order traversal: left subtree, node, then right subtree
        result = []
        if self.left:
            result.extend(self.left.inorder())
        result.append(self.key)
        if self.right:
            result.extend(self.right.inorder())
        return result


class TreeSort:
    def __init__(self, arr):
        self.arr = arr
        self.root = None

    def sort(self):
        # Build the BST by inserting every element
        for key in self.arr:
            self._insert(key)
        # Perform in-order traversal to get the sorted array
        return self._inorder(self.root)

    def _insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root.insert(key)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.key] + self._inorder(node.right)
