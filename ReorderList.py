class ListNode:
    def __init__(self, val):
        self.val=val
        self.next=None
def reorderList(head):
    if not head or not head.next:
        return 
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    secondHalf = reverseList(slow.next)
    slow.next=None
    mergeLists(head, secondHalf)
def reverseList(head):
    prev=None
    current=head
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    return prev
def mergeLists(first, second):
    while second:
        temp1=first.next
        temp2=second.next
        first.next=second
        second.next=temp1
        first=temp1
        second=temp2
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

values = input().split()
head = ListNode(int(values[0]))
current=head
for val in values[1:]:
    current.next=ListNode(int(val))
    current=current.next
reorderList(head)
printList(head)