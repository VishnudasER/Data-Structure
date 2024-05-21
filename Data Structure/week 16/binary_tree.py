class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def contains(self, key):
        return self._contains_recursive(self.root, key)

    def _contains_recursive(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._contains_recursive(node.left, key)
        else:
            return self._contains_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._delete_recursive(node.right, min_node.key)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.key)
            self._inorder_traversal_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result

    def _preorder_traversal_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_traversal_recursive(node.left, result)
            self._preorder_traversal_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal_recursive(self.root, result)
        return result

    def _postorder_traversal_recursive(self, node, result):
        if node:
            self._postorder_traversal_recursive(node.left, result)
            self._postorder_traversal_recursive(node.right, result)
            result.append(node.key)

# Example usage:
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Inorder traversal:", bst.inorder_traversal())  # Output: [2, 3, 4, 5, 6, 7, 8]
print("Preorder traversal:", bst.preorder_traversal())  # Output: [5, 3, 2, 4, 7, 6, 8]
print("Postorder traversal:", bst.postorder_traversal())  # Output: [2, 4, 3, 6, 8, 7, 5]

print("Contains 4:", bst.contains(4))  # Output: True
print("Contains 9:", bst.contains(9))  # Output: False

bst.delete(7)
bst.delete(8)
print("Inorder traversal after deleting 7:", bst.inorder_traversal())  # Output: [2, 3, 4, 5, 6, 8]
