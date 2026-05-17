from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.curComb = []
        self.ans = []
        self.bt(0)
        return self.ans

    def constructSolution (self):
        board = [["."] * self.n for _ in range(self.n)]

        for placements in self.curComb:
            board[placements[0]][placements[1]] = 'Q'

        self.ans.append([])
        for row in board:
            self.ans[-1].append("".join(row))
    

    def bt(self, index):
        if index == self.n:
            self.constructSolution()
            return

        for i in range(self.n):
            if self.isValidPlacement ((index, i)):    
                self.curComb.append((index, i))
                self.bt(index + 1)
                self.curComb.pop()


    def isValidPlacement(self, nextPlacement):
        i = 1

        for placement in self.curComb[::-1]:
            if placement[1] == nextPlacement[1]:
                return False
            
            if placement[0] == nextPlacement[0] - i:
                if placement[1] == nextPlacement[1] + i or placement[1] == nextPlacement[1] - i:
                    return False

            i += 1

        return True

        