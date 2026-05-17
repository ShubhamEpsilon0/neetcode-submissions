class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid

        maxMin = 0
        totalFreshFruits = 0
        #multi-source bfs
        self.q = []
        self.nq = []
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 2:
                    self.q.append((i,j))
                elif self.grid[i][j] == 1:
                    totalFreshFruits+=1

        while self.q:
            rottenCount = 0
            while self.q:
                r,c = self.q.pop()
                rottenCount += self.AddToRottenQueue(r + 1,c)
                rottenCount += self.AddToRottenQueue(r - 1,c)
                rottenCount += self.AddToRottenQueue(r,c + 1)
                rottenCount += self.AddToRottenQueue(r,c - 1)
            
            totalFreshFruits -= rottenCount
            self.q=self.nq
            self.nq = []
            maxMin += 1 if rottenCount > 0 else 0

        return maxMin if totalFreshFruits == 0 else -1

    def AddToRottenQueue(self, r, c):
        if r < 0 or r >= self.m or c < 0 or c >= self.n:
            return 0

        if self.grid[r][c] == 1:
            self.grid[r][c] = 2
            self.nq.append((r,c))
            return 1

        return 0


        
        