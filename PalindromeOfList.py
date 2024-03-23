class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Main:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def add_node(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.size+=1
    def reverse_list(self, temp):
        current=temp
        prev_node=None
        next_node=None
        while current:
            next_node=current.next
            current.next=prev_node
            prev_node=current
            current=next_node
        return prev_node
    def is_palindrome(self):
        current=self.head
        flag=True
        mid=self.size//2 if self.size%2==0 else (self.size+1)//2
        for _ in range(1,mid):
            current=current.next
        rev_head=self.reverse_list(current.next)
        while self.head and rev_head:
            if self.head.data!=rev_head.data:
                flag=False
                break
            self.head=self.head.next
            rev_head=rev_head.next
        if flag:
            print("true")
        else:
            print("false")
if __name__=="__main__":
    s_list = Main()
    numbers_str=input().split()
    for num_str in numbers_str:
        num = int(num_str)
        s_list.add_node(num)
    s_list.is_palindrome()