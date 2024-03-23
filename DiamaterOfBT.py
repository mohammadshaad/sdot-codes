from collections import deque
class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class Solution:   
    class A:
        def __init__(self):
            self.ans=0 
    @staticmethod
    def height(root,a):
        if not root:
            return 0
        left=Solution.height(root.left, a)
        right=Solution.height(root.right,a)
        a.ans=max(a.ans,left+right+1)
        return 1+max(left,right)
    @staticmethod
    def diameter(root):
        if not root:
            return 0
        a=Solution.A()
        Solution.height(root,a)
        return a.ans
def buildTree(s):
    if not s or s[0]=='N':
        return None
    ip=s.split()
    root=Node(int(ip[0]))
    queue=deque([root])
    i=1
    while queue and i<len(ip):
        currNode = queue.popleft()
        currVal=ip[i]
        if currVal != 'N':
            currNode.left=Node(int(currVal))
            queue.append(currNode.left)
        i+=1
        if i>=len(ip):
            break
        currVal=ip[i]
        if currVal != 'N':
            currNode.right=Node(int(currVal))
            queue.append(currNode.right)
        i+=1
    return root
if __name__ == "__main__":
    s1=input().strip()
    root1=buildTree(s1)
    g=Solution()
    print(g.diameter(root1))
    