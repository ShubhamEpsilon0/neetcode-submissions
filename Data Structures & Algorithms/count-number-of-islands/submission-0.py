class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        count = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == "1" and (i,j) not in self.visited:
                    count += 1
                    self.visitEntireIsland(i,j)

        return count


    def visitEntireIsland (self, startR, startC):
        self.visited.add((startR, startC))

        directionSteps = [(1,0),(-1,0),(0,1),(0,-1)]

        for direction in directionSteps:
            if (
                (startR + direction[0] < self.m and startR + direction[0] >= 0) and 
                (startC + direction[1] < self.n) and (startC + direction[1] >=0) and
                self.grid[startR + direction[0]][startC + direction[1]] == "1" and
                (startR + direction[0], startC + direction[1]) not in self.visited
            ):
                self.visitEntireIsland(startR + direction[0], startC + direction[1])

    


        