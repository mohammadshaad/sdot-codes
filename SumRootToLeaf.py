class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def tree_paths_sum_util(self, node, val):
        if node is None:
            return 0
        val = val * 10 + node.data
        if node.left is None and node.right is None:
            return val
        return self.tree_paths_sum_util(node.left, val) + self.tree_paths_sum_util(node.right, val)

    def tree_paths_sum(self):
        return self.tree_paths_sum_util(self.root, 0)

def insert_node(root, data):
    if root is None:
        return Node(data)

    queue = [root]
    while queue:
        temp = queue.pop(0)

        if temp.left is None:
            temp.left = Node(data)
            break
        else:
            queue.append(temp.left)

        if temp.right is None:
            temp.right = Node(data)
            break
        else:
            queue.append(temp.right)

def main():
    s = input().strip()

    tree = BinaryTree()
    tree.root = Node(int(s[0]))

    index = 1
    while index < len(s):
        insert_node(tree.root, int(s[index]))
        index += 1

    print(tree.tree_paths_sum())

if __name__ == "__main__":
    main()