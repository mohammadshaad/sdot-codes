class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def kthSmallest(root, k):
    result = [0, 0]
    result[0] = 0
    kthSmallestHelper(root, k, result)
    return result[1]

def kthSmallestHelper(root, k, result):
    if root is None or result[0] == k:
        return
    kthSmallestHelper(root.left, k, result)
    result[0] += 1
    if result[0] == k:
        result[1] = root.val
        return
    kthSmallestHelper(root.right, k, result)

root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)

k = 3
result = kthSmallest(root, k)
print(result)
