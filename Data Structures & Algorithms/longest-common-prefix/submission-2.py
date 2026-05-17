class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ""
        i = 0
        mismatch = False
        minLen = min([len(s) for s in strs])
        while i < minLen:
            for st in strs[1:]:
                if st[i] != strs[0][i]:
                    mismatch = True
                    break

            if mismatch:
                break
            longestPrefix += strs[0][i]
            i += 1

        return longestPrefix
        