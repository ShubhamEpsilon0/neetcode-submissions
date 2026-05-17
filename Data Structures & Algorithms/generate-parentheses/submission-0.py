class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.n = n
        self.bt(0,0,"")
        return self.ans

    def bt(self, openCount, closeCount, curStr):
        if closeCount > openCount:
            return
        if len(curStr) == 2*self.n:
            if openCount == closeCount:
                self.ans.append(curStr)
            return

        self.bt(openCount + 1, closeCount, curStr + '(')
        self.bt(openCount, closeCount + 1, curStr + ')')

    
        