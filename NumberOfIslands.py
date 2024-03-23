class Solution:
    def __init__(self):
        self.dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    def toString(self, r, c):
        return str(r) + " " + str(c)
    
    def dfs(self, grid, x0, y0, i, j, v):
        rows, cols = len(grid), len(grid[0])
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] <= 0:
            return
        grid[i][j] *= -1
        v.append(self.toString(i - x0, j - y0))
        for dx, dy in self.dirs:
            self.dfs(grid, x0, y0, i + dx, j + dy, v)
    
    def countDistinctIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        coordinates = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    v = []
                    self.dfs(grid, i, j, i, j, v)
                    coordinates.add(tuple(v))
        return len(coordinates)

if __name__ == "__main__":    
    n = int(input())
    m = int(input())
    grid = []
    for _ in range(n):
        row_input = list(map(int, input().split()))
        grid.append(row_input)
    solution = Solution()
    ans = solution.countDistinctIslands(grid)
    print(ans)