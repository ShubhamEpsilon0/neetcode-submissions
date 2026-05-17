class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])


        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    self.updateNodes (i,j, 1)

    def updateNodes(self, r, c, dist):
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for d in dirs:
            new_r,new_c = r + d[0], c + d[1]
            if new_r < 0 or new_r >= self.m or new_c < 0 or new_c >= self.n:
                continue
            if self.grid[new_r][new_c] > dist:

                self.grid[new_r][new_c] = dist
                self.updateNodes(new_r,new_c,dist + 1)

        
        