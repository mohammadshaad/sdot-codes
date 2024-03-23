class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.data < l2.data:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

def mergeKLists(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 2:
        return mergeTwoLists(lists[0], lists[1])
    
    mid = len(lists) // 2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])
    
    return mergeTwoLists(left, right)

def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

k = int(input())
lists = []

for i in range(k):
    size = int(input())
    list_elements = list(map(int, input().split()))
    list_elements = list_elements[:size]
    head = Node(list_elements[0])
    current = head
    for element in list_elements[1:]:
        current.next = Node(element)
        current = current.next
    lists.append(head)

merged_list = mergeKLists(lists)

printList(merged_list)