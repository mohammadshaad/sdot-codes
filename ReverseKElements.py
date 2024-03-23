class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    if not head or k == 1:
        return head

    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy

    while head:
        tail = prev
        for _ in range(k):
            tail = tail.next
            if not tail:
                return dummy.next

        next_head = tail.next
        tail.next = None

        prev.next, head = reverseList(head)
        head.next = next_head
        prev = head

        head = next_head

    return dummy.next

def reverseList(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev, head

def printList(head):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()

# Input processing
elements = list(map(int, input().split()))
k = int(input())

# Create linked list
head = ListNode(elements[0])
current = head
for val in elements[1:]:
    current.next = ListNode(val)
    current = current.next

# Reverse in groups of k and print
reversed_head = reverseKGroup(head, k)
printList(reversed_head)