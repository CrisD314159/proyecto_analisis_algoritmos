class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.key)
        inorder_traversal(root.right, result)


def tree_sort(arr):
    if not arr:
        return []
    root = None
    for key in arr:
        root = insert(root, key)
    sorted_arr = []
    inorder_traversal(root, sorted_arr)
    arr[:] = sorted_arr  # Copy back sorted elements
