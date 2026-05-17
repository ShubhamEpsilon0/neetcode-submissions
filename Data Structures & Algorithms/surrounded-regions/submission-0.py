class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.unSurroundedCells = set()
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        #Row Major Search
        for i in [0, self.rows - 1]:
            for j in range(self.cols):
                if self.board[i][j] == "O":
                    self.dfs(i,j)

        #Col Major Search
        for i in range(self.rows):
            for j in [0, self.cols - 1]:
                if self.board[i][j] == "O":
                    self.dfs(i,j)


        for i in range(self.rows):
            for j in range(self.cols):
                if (i,j) not in self.unSurroundedCells:
                    self.board[i][j] = 'X'

    def dfs (self, r, c):
        self.unSurroundedCells.add((r,c))
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        for dr,dc in dirs:
            nr,nc =r + dr, c + dc
            if nr < 0 or nr >= self.rows or nc < 0 or nc >= self.cols:
                continue

            if self.board[nr][nc] == "X":
                continue

            if (nr,nc) in self.unSurroundedCells:
                continue

            self.dfs(nr, nc)

            

        


        

        
        