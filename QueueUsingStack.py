class QueueUsingStacks:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self,x):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    def pop(self):
        if self.stack1:
            return self.stack1.pop()
        else:
            return -1
if __name__ == "__main__":
    q=int(input().strip())
    queue=QueueUsingStacks()
    output=[]
    for _ in range(q):
        query=input().strip().split()
        if query[0]=='1':
            queue.push(int(query[1]))
        elif query[0]=='2':
            output.append(queue.pop())
    print(' '.join(map(str,output)))