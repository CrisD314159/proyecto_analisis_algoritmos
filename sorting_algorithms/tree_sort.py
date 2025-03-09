"""
Tree sort module
"""


class TreeSort:
    """
    A class that implements the Tree Sort algorithm.
    """

    class Node:
        """
        Node class for the binary search tree.
        """

        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    @staticmethod
    def insert(root, key):
        """
        Insert a key into the binary search tree.
        """
        if root is None:
            return TreeSort.Node(key)
        if key < root.key:
            root.left = TreeSort.insert(root.left, key)
        else:
            root.right = TreeSort.insert(root.right, key)
        return root

    @staticmethod
    def inorder_traversal(root, result):
        """
        Perform inorder traversal of the binary search tree.
        """
        if root:
            TreeSort.inorder_traversal(root.left, result)
            result.append(root.key)
            TreeSort.inorder_traversal(root.right, result)

    @staticmethod
    def sort(arr):
        """
        Tree sort algorithm implementation.
        """
        if not arr:
            return []

        # Build the binary search tree
        root = None
        for key in arr:
            root = TreeSort.insert(root, key)

        # Traverse the tree to get sorted elements
        sorted_arr = []
        TreeSort.inorder_traversal(root, sorted_arr)

        # Copy sorted elements back to original array
        arr[:] = sorted_arr
        return sorted_arr
