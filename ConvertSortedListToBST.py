class LinkedList:
    def __init__(self):
        self.head = None

    class LNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    class TNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def sortedListToBST(self):
        n = self.countNodes(self.head)
        return self.sortedListToBSTRecur(n)

    def sortedListToBSTRecur(self, n):
        if n <= 0:
            return None
        left = self.sortedListToBSTRecur(n // 2)
        root = self.TNode(self.head.data)
        root.left = left
        self.head = self.head.next
        root.right = self.sortedListToBSTRecur(n - n // 2 - 1)
        return root

    def countNodes(self, head):
        count = 0
        temp = head
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    def push(self, new_data):
        new_node = self.LNode(new_data)
        new_node.prev = None
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def printList(self, node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next

    def preOrder(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)

if __name__ == "__main__":
    llist = LinkedList()
    elements = list(map(int, input().split()))
    for element in reversed(elements):
        llist.push(element)

    root = llist.sortedListToBST()
    llist.preOrder(root)
    print()
