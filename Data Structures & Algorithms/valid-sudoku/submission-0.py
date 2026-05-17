class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        grid = [set() for i in range(9)] # encoding - row // 3 * 3+ col // 3
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    print(board[i][j], " already in row ", i)
                    return False

                if board[i][j] in cols[j]:
                    print(board[i][j], " already in col ", j)
                    return False

                gridNum = i // 3 * 3 + j // 3
                if board[i][j] in grid[gridNum]:
                    print(board[i][j], " already in grid ", gridNum)
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grid[gridNum].add(board[i][j])
        
        return True

                