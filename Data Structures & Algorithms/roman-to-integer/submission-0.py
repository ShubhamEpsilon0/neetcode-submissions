class Solution:
    def romanToInt(self, s: str) -> int:
        R2IMap = { "I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        ans = 0
        prevElem = None
        for c in s:
            if prevElem and R2IMap[prevElem] < R2IMap[c]:
                ans -= R2IMap[prevElem]*2
            
            ans += R2IMap[c]
            prevElem = c
        return ans

        