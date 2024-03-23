class ListNode:
    def __init__(self, val):
        self.val=val
        self.next=None
def rotateRight(head, k):
    if not head or not head.next or k==0:
        return head
    length=1
    tail=head
    while tail.next:
        tail=tail.next
        length+=1
    k=k%length
    if k==0:
        return head
    newTail=head
    for _ in range(length-k-1):
        newTail = newTail.next
    newHead = newTail.next
    newTail.next=None
    tail.next=head
    return newHead
def printList(head):
    temp=head
    while temp:
        print(temp.val, end=" ")
        temp=temp.next
values = list(map(int, input().split()))
head = ListNode(values[0])
current = head
for val in values[1:]:
    if val == -1:
        break
    current.next = ListNode(val)
    current = current.next

k = 2
head = rotateRight(head, k)
printList(head)
