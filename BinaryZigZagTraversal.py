class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = [root]
    left_to_right = True

    while queue:
        current_level = []
        next_level = []

        while queue:
            node = queue.pop(0)
            current_level.append(node.val)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if not left_to_right:
            current_level.reverse()

        result.extend(current_level)
        queue = next_level
        left_to_right = not left_to_right

    return result

# Driver code
if __name__ == "__main__":
    nodes = input().split()
    root = TreeNode(int(nodes[0]))
    queue = [root]
    index = 1
    
    while index < len(nodes):
        node = queue.pop(0)
        left_val = nodes[index]
        index += 1
        if left_val != "N":
            node.left = TreeNode(int(left_val))
            queue.append(node.left)
        
        if index < len(nodes):
            right_val = nodes[index]
            index += 1
            if right_val != "N":
                node.right = TreeNode(int(right_val))
                queue.append(node.right)

    result = zigzagLevelOrder(root)
    print(' '.join(map(str, result)))