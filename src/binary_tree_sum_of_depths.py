class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_depths(root: TreeNode) -> int:
    if root is None:
        return 0

    return depth_search(root, 0)

def depth_search(node, depth):
    if node is None:
        return 0
    return depth + depth_search(node.left, depth + 1) + depth_search(node.right, depth + 1)