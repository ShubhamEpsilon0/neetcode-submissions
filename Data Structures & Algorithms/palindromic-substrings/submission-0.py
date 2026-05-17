class Solution:
    def countPalin(self,s, l, r):
        count = 0
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        return count
    
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for mid in range(len(s)):
            # odd len palins
            count += self.countPalin(s, mid, mid)
            ## even len palin
            count += self.countPalin(s, mid, mid + 1)

        return count
            

        