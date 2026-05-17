class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prevRow = [0] * (len(text1) + 1)

        for i in range(len(text2) - 1, -1, -1):
            curRow = [0] * (len(text1) + 1)
            for j in range(len(text1) - 1, -1, -1):
                if text1[j] == text2[i]:
                    curRow[j] = 1 + prevRow[j + 1]
                else:
                    curRow[j] = max(
                        curRow[j + 1],
                        prevRow[j],
                        prevRow[j + 1]
                    )
            prevRow = curRow

        return prevRow[0]


