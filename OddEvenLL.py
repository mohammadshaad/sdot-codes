class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class Solution:
    def oddEvenList(self,head):
        if not head or not head.next:
            return head
        even_head,even_tail=None,None
        odd_head,odd_tail=None,None
        current=head
        while current:
            if current.val%2==0:
                if not even_head:
                    even_head=current
                    even_tail=current
                else:
                    even_tail.next=current
                    even_tail=even_tail.next
            else:
                if not odd_head:
                    odd_head=current
                    odd_tail=current
                else:
                    odd_tail.next=current
                    odd_tail=odd_tail.next
            current=current.next
        if even_tail:
            even_tail.next=odd_head
        else:
            even_head=odd_head
        if odd_tail:
            odd_tail.next=None
        return even_head
def printLinkedList(head):
    while head:
        print(head.val,end=" ")
        head=head.next
    print()
input_list = input().split()
head=None
current=None
for val_str in input_list:
    val=int(val_str)
    if not head:
        head=ListNode(val)
        current=head
    else:
        current.next=ListNode(val)
        current=current.next
solution=Solution()
result=solution.oddEvenList(head)
printLinkedList(result)
