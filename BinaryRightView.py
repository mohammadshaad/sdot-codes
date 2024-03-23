from collections import deque
class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def rightView(self, root):
        if not root:
            return []
        result=[]
        queue=deque()
        queue.append(root)
        while queue:
            n=len(queue)
            for i in range(n):
                curr=queue.popleft()
                if i==n-1:
                    result.append(curr.data)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result
    def buildTree(self, s):
        if not s or s[0] == 'N':
            return None
        ip=s.split()
        root = Node(int(ip[0]))
        queue=deque([root])
        i=1
        while queue and i<len(ip):
            currNode=queue.popleft()
            currVal=ip[i]
            if currVal!='N':
                currNode.left=Node(int(currVal))
                queue.append(currNode.left)
            i+=1
            if i>=len(ip):
                break
            currVal=ip[i]
            if currVal!='N':
                currNode.right=Node(int(currVal))
                queue.append(currNode.right)
            i+=1
        return root
if __name__ == "__main__":
    t=int(input().strip())
    for _ in range(t):
        s=input().strip()
        solution = Solution()
        root=solution.buildTree(s)
        arr=solution.rightView(root)
        for x in arr:
            print(x, end=" ")
        print()