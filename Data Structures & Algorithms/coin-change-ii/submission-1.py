class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            curRow = [0] * (amount + 1)
            curRow[0] = 1
            for j in range(1, amount + 1):
                curRow[j] = dp[j] + (curRow[j - coin] if j - coin >= 0 else 0)
            dp = curRow

        return dp[-1]
        