class Solution:
    def getMaxPalinWithMid(self, s, l, r):
        n = len(s)
        if l < 0 or r ==n or s[l] != s[r]:
            return "", 0

        while l >= 0 and r < n:
            if s[l] != s[r]:
                break
            l-=1
            r+=1
        l+=1
        r-=1

        return s[l:r + 1], r+1-l

    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ansLen = 0
        n = len(s)

        for i in range(n):
            oddPalin, oddPalinLen = self.getMaxPalinWithMid(s, i, i)
            evenPalin, evenPalinLen = self.getMaxPalinWithMid(s,i,i+1)
            
            if ansLen < oddPalinLen:
                ansLen = oddPalinLen
                ans = oddPalin
            
            if ansLen < evenPalinLen:
                ansLen = evenPalinLen
                ans = evenPalin

        return ans
        


        