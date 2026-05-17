class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        self.visited = [[0] * n for _ in range(m)]
        self.grid = grid
        self.m = m
        self.n = n
        ans = 0

        for i in range(m):
            for j in range(n):
                if not self.visited[i][j]:
                    ans = max(ans, self.calculateIslandArea(i,j))

        return ans

    def calculateIslandArea(self, rowIndex, colIndex):
        if rowIndex < 0 or rowIndex >= self.m or colIndex < 0 or colIndex >= self.n:
            return 0

        if self.visited[rowIndex][colIndex] or not self.grid[rowIndex][colIndex]:
            return 0

        self.visited[rowIndex][colIndex] = 1

        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        ans = 1
        for d in dirs:
            ans += self.calculateIslandArea(rowIndex + d[0], colIndex+d[1])

        return ans


        