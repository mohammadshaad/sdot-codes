class ListNode:
    def __init__(self,x):
        self.val = x
        self.next=None
def merge_two_lists(l1, l2):
    dummy=ListNode(0)
    current=dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next=l1
            l1=l1.next
        else:
            current.next=l2
            l2=l2.next
        current=current.next
    if l1:
        current.next=l1
    else:
        current.next=l2
    return dummy.next
def create_linked_list(length, values):
    dummy=ListNode(0)
    current = dummy
    for val in values:
        current.next=ListNode(val)
        current=current.next
    return dummy.next
if __name__ == "__main__":
    n=int(input())
    values_l1 = list(map(int,input().split()))
    l1=create_linked_list(n,values_l1)
    m=int(input())
    values_l2=list(map(int,input().split()))
    l2=create_linked_list(m,values_l2)
    merged=merge_two_lists(l1,l2)
    while merged:
        print(merged.val, end=" ")
        merged=merged.next