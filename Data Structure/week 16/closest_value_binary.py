class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def closest_value_in_tree(root, target):
    closest = float('inf')  # Initialize closest to positive infinity
    current = root
    
    while current:
        if abs(current.key - target) < abs(closest - target):
            closest = current.key

        if target < current.key:
            current = current.left
        elif target > current.key:
            current = current.right
        else:
            break  # Found exact match, no need to continue

    return closest

# Example usage:
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

target = 9
closest = closest_value_in_tree(root, target)
print("Closest value to", target, "in the tree is:", closest)  # Output: Closest value to 9 in the tree is: 10
