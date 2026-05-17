class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i = 0
        while i < n - m + 1:
            if needle[0] == haystack[i]:
                nextPossibleStart = i
                j = 1
                while j < m:
                    if needle[0] == haystack[i + j] and nextPossibleStart == i:
                        nextPossibleStart = i + j - 1
                    if needle[j] != haystack[j + i]:
                        break

                    j += 1

                if j == m:
                    return i
                i = nextPossibleStart
            i += 1
        
        return -1


        