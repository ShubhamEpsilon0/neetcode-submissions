from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        replacementIndexQueue = []
        L = 0
        freqMap = defaultdict (int)
        ans = 0

        for R in range(len(s)):
            freqMap[s[R]] += 1
            while k - (R - L + 1 - max(freqMap.values())) < 0:
                freqMap[s[L]] -= 1
                L += 1
            ans = max(ans, R - L + 1)

        return ans


