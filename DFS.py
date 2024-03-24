from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.adjLists = defaultdict(list)
        self.visited = [False] * vertices
    
    def addEdge(self, src, dest):
        self.adjLists[src].append(dest)
    
    def DFS(self, vertex):
        self.visited[vertex] = True
        print(vertex, end=" ")
        for adj in self.adjLists[vertex]:
            if not self.visited[adj]:
                self.DFS(adj)

if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.DFS(2)
    print()
