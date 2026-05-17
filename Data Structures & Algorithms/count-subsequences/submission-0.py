class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp_old = [1] * (len(s) + 1)

        for i in range(len(t) - 1, -1, -1):
            dp_new = [0] * (len(s) + 1)
            for j in range(len(s) - 1, -1, -1):
                if t[i] == s[j]:
                    dp_new[j] += dp_old[j + 1]
                dp_new[j] += dp_new[j + 1]

            dp_old = dp_new

        return dp_old[0]
        