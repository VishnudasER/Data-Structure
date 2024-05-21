class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_bst(root):
    # Helper function to perform inorder traversal
    def inorder_traversal(node, values):
        if node:
            inorder_traversal(node.left, values)
            values.append(node.key)
            inorder_traversal(node.right, values)
    
    values = []
    inorder_traversal(root, values)
    
    # Check if the values are sorted
    for i in range(1, len(values)):
        if values[i] <= values[i - 1]:
            return False
    
    return True

# Example usage:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)

print("Is the given tree a BST?", is_bst(root))  # Output: True
