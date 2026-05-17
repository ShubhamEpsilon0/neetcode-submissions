class Solution:
    def numDecodings(self, s: str) -> int:
        self.str = s
        self.strLen = len(s)
        self.cache = {}
        return self.dp(0)

    def dp(self, strIndex):
        if strIndex in self.cache:
            return self.cache[strIndex]
        if strIndex >= self.strLen:
            return 1

        if self.str[strIndex] == "0":
            return 0

        ans = self.dp(strIndex + 1)

        if strIndex != self.strLen - 1 and self.str[strIndex] <= "2" and not (self.str[strIndex] == "2" and self.str[strIndex + 1] > "6"):
            ans += self.dp(strIndex + 2)
        self.cache[strIndex] = ans
        return ans
        