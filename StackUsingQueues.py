class StackUsingQueues:
    def __init__(self):
        self.primary_queue = []
        self.temp_queue = []

    def push(self, x):
        while self.primary_queue:
            self.temp_queue.append(self.primary_queue.pop(0))

        self.primary_queue.append(x)

        while self.temp_queue:
            self.primary_queue.append(self.temp_queue.pop(0))

    def pop(self):
        if self.primary_queue:
            return self.primary_queue.pop(0)
        else:
            return -1

if __name__ == "__main__":
    q = int(input().strip())
    stack = StackUsingQueues()
    output = []
    for _ in range(q):
        query = input().strip().split()
        if query[0] == '1':
            stack.push(int(query[1]))
        elif query[0] == '2':
            output.append(stack.pop())

    
    print(' '.join(map(str, output)))