class Solution:
    Dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.cache = {}

        longestPath = 1
        for i in range(self.rows):
            for j in range(self.cols):
                longestPath = max(longestPath, self.explorePath(i,j))

        return longestPath

    def IsOutOfBounds(self, curRow, curCol):
        return curRow < 0 or curRow >= self.rows or curCol < 0 or curCol >= self.cols

    def explorePath (self, curRow, curCol):
        if (curRow, curCol) in self.cache:
            return self.cache[(curRow, curCol)]

        longestPath = 1
        for dr, dc in Solution.Dirs:
            newRow, newCol = curRow + dr, curCol + dc
            if self.IsOutOfBounds(newRow, newCol):
                continue
            
            if self.matrix[curRow][curCol] >= self.matrix[newRow][newCol]:
                continue

            longestPath = max(longestPath, 1 + self.explorePath(newRow, newCol))

        self.cache[(curRow, curCol)] = longestPath
        return longestPath
        
        
        