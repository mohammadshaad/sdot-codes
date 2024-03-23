class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(nodes, index):
    if index < len(nodes):
        if nodes[index] == 'N':
            return None
        root = TreeNode(nodes[index])
        root.left = buildTree(nodes, 2*index+1)
        root.right = buildTree(nodes, 2*index+2)
        return root
    
    return None

def flatten(root):
    if not root:
        return
    flatten(root.left)
    flatten(root.right)
    
    right_subtree = root.right
    root.right = root.left
    root.left = None
    
    while root.right:
        root = root.right
    root.right = right_subtree
        
def print_linked_list(root):
    while root:
        print(root.val, end='')
        root = root.right
    print()
        
nodes_input = input()
root = buildTree(nodes_input, 0)
flatten(root)
print_linked_list(root)