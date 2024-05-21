class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

# Example usage:
root = None
keys_to_insert = [5, 3, 7, 2, 4, 6, 8]
for key in keys_to_insert:
    root = insert(root, key)
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

# Example usage:
root = deleteNode(root, 7)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)

# Example usage:
print("Inorder Traversal:", end=" ")
inorder_traversal(root)
