class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.bt(0, s, [""])
        return self.ans

    def checkPalindrome(self, s):
        i = 0
        while i < len(s) // 2:
            if s[i] != s[len(s) -i -1]:
                return False
            i += 1

        return True

    def bt(self, index, s, curSet):
        if index == len(s):
            if curSet[-1] != "":
                if self.checkPalindrome(curSet[-1]):
                    self.ans.append(curSet.copy())
            return

        curSetCopy = curSet.copy()
        curSetCopy[-1] += s[index]

        # don't partition
        self.bt(index + 1, s, curSetCopy)

        #partition
        if self.checkPalindrome(curSetCopy[-1]):
            curSetCopy.append("")
            self.bt(index + 1, s, curSetCopy)
        
        
        

        

        

        