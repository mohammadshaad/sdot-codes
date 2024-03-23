class Solution:
    def canFinish(self, n, prerequisites):
        # Create adjacency list and indegree array
        adj_list = [[] for _ in range(n)]
        indegree = [0] * n
        
        # Populate adjacency list and indegree array
        for pair in prerequisites:
            course, prereq = pair
            adj_list[prereq].append(course)
            indegree[course] += 1
        
        # Initialize BFS queue with courses having no prerequisites
        bfs_queue = [course for course in range(n) if indegree[course] == 0]
        
        # Perform BFS
        while bfs_queue:
            course = bfs_queue.pop(0)
            n -= 1  # Decrement the count of remaining courses
            for next_course in adj_list[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    bfs_queue.append(next_course)
        
        # If all courses have been taken (n == 0), print 1, else print 0
        if n == 0:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    prerequisites = []
    print()
    for _ in range(M):
        a, b = map(int, input().split())
        prerequisites.append([a, b])
        
    obj = Solution()
    obj.canFinish(N, prerequisites)