from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        currentCharsFreqMap = defaultdict(int)
        curUniqueSet = set()
        start = 0
        maxLen = 0

        for end in range(len(s)):
            currentCharsFreqMap[s[end]] += 1
            curUniqueSet.add(s[end])

            while start <= end and len(curUniqueSet) > k:
                currentCharsFreqMap[s[start]] -= 1
                if currentCharsFreqMap[s[start]] <= 0:
                    del currentCharsFreqMap[s[start]]
                    curUniqueSet.remove(s[start])
                start += 1

            maxLen = max(maxLen, end - start + 1)
        return maxLen
         


        