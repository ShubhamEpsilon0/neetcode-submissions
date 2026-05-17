from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        needMap = Counter(t)
        needCount = len(t)
        L = 0
        foundCount = 0
        minStr= ""
        for R in range(len(s)):
            if s[R] in needMap.keys():
                needMap[s[R]] -= 1
                if needMap[s[R]] >= 0:
                    foundCount += 1

            while L<= R and (s[L] not in needMap.keys() or needMap[s[L]] < 0):
                if s[L] in needMap.keys():
                    needMap[s[L]] += 1
                L += 1

            if foundCount == needCount and (minStr == "" or R - L + 1 < len(minStr)):
                minStr=s[L: R + 1]

        return minStr


            

            


        