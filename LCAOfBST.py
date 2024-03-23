
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(arr):
    if not arr or arr[0] == 'N':
        return None

    root = TreeNode(int(arr[0]))
    queue = [root]
    i = 1
    while queue and i < len(arr):
        currNode = queue.pop(0)

        if arr[i] != '-1':
            currNode.left = TreeNode(int(arr[i]))
            queue.append(currNode.left)
        i += 1
        
        if i >= len(arr):
            break
        if arr[i] != '-1':
            currNode.right = TreeNode(int(arr[i]))
            queue.append(currNode.right)
        i += 1

    return root

def findLCA(node, n1, n2):
    if not node:
        return None
    if node.data == n1 or node.data == n2:
        return node
    
    left_lca = findLCA(node.left, n1, n2)
    right_lca = findLCA(node.right, n1, n2)
    
    if left_lca and right_lca:
        return node
    return left_lca if left_lca else right_lca

if __name__ == "__main__":
    s = input().split()
    root = buildTree(s)
    x, y = map(int, input().split())
    ans = findLCA(root, x, y)
    print(ans.data if ans else None)