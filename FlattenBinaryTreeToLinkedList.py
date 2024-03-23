class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten_binary_tree_to_linked_list(root):
    if not root:
        return None
    
    # Stack to store nodes during inorder traversal
    stack = []
    current = root
    
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            if current.right:
                temp = current.right
                current.right = current.left
                current.left = None
                while current.right:
                    current = current.right
                current.right = temp
            current = current.right

    # Printing the linked list in preorder sequence
    current = root
    while current:
        print(current.val, end=' ')
        current = current.right
    print()

# Function to build the tree from the input string
def build_tree(s):
    stack = []
    root = TreeNode(int(s[0]))
    stack.append(root)
    i = 1
    while stack and i < len(s):
        node = stack.pop()
        if s[i] != 'N':
            node.left = TreeNode(int(s[i]))
            stack.append(node.left)
        i += 1
        if i < len(s) and s[i] != 'N':
            node.right = TreeNode(int(s[i]))
            stack.append(node.right)
        i += 1
    return root

# Taking input from the user
input_str = "12534N6NNNNNNN7"  # Input string

# Build the binary tree from the input string
root = build_tree(input_str)

# Flatten the binary tree to linked list and print the result
flatten_binary_tree_to_linked_list(root)