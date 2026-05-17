class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        grid = [0] * 9 # encoding - row // 3 * 3+ col // 3
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j]) - 1

                gridNum = i // 3 * 3 + j // 3
                if (1 << val) & rows[i] or (1 << val) & cols[j] or (1 << val) & grid[gridNum]:
                    return False
                rows[i] |= (1 << val) 
                cols[j] |= (1 << val)
                grid[gridNum] |= (1 << val)
        
        return True

                