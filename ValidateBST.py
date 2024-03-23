class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(nodes):
    if not nodes:
        return None
    
    root = BinaryTreeNode(int(nodes[0]))
    queue = [root]
    index = 1
    
    while index < len(nodes):
        node = queue.pop(0)
        
        left_val = nodes[index]
        index += 1
        if left_val != "-1":
            node.left = BinaryTreeNode(int(left_val))
            queue.append(node.left)
        
        if index < len(nodes):
            right_val = nodes[index]
            index += 1
            if right_val != "-1":
                node.right = BinaryTreeNode(int(right_val))
                queue.append(node.right)
    
    return root

def helper(root, min_val, max_val):
    if root is None:
        return True
    
    if not min_val <= root.data <= max_val:
        return False
    
    return helper(root.left, min_val, root.data - 1) and helper(root.right, root.data + 1, max_val)

def validate_BST(root):
    return helper(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        nodes = input().split()
        root = build_tree(nodes)
        print("true" if validate_BST(root) else "false")