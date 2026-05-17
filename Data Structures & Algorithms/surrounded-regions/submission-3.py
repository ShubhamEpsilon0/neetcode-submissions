class Solution:
    def solve(self, board: List[List[str]]) -> None:
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
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                elif self.board[i][j] == 'T':
                    self.board[i][j] = 'O'

    def dfs (self, r, c):
        self.board[r][c] = 'T'
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        for dr,dc in dirs:
            nr,nc = dr + r, dc+c
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.board[nr][nc] == 'O':
                self.dfs(nr, nc)

            

        


        

        
        