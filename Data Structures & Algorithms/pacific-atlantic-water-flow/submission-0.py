class Solution:
    dirs =[(1,0),(-1,0),(0,1),(0, -1)]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.rows = len(heights)
        self.cols = len(heights[0])

        self.createInitialPossiblePathsFromNodes()
        ans = []

        for i in range(self.rows):
            for j in range(self.cols):
                if all(self.searchPath(i, j)):
                    ans.append([i,j])

        return ans

    def searchPath(self, row, col):
        if all(self.possiblePathsFromNodes[row][col]):
            return [True, True]

        ans = self.possiblePathsFromNodes[row][col]
        temp = self.heights[row][col]
        self.heights[row][col] = float("INF")

        for dr, dc in Solution.dirs:
            nr, nc = row+dr, col+dc
            if nr < 0 or nr == self.rows or nc < 0 or nc == self.cols:
                continue
            if self.heights[nr][nc] <= temp:
                res = self.searchPath(nr, nc)
                ans[0] |= res[0]
                ans[1] |= res[1]

            if all(ans):
                break

        self.heights[row][col] = temp
        self.possiblePathsFromNodes[row][col] = ans
        return ans
        

    def createInitialPossiblePathsFromNodes(self):
        self.possiblePathsFromNodes = []

        for i in range(self.rows):
            self.possiblePathsFromNodes.append([])
            for j in range(self.cols):
                pacificPathPossible=i == 0 or j == 0
                atlanticPathPossible=i == self.rows -1 or j == self.cols -1
                self.possiblePathsFromNodes[-1].append([pacificPathPossible, atlanticPathPossible])






        