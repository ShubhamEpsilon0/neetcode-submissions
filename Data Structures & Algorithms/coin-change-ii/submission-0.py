class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.coins = coins
        self.cache = {}
        return self.dp(0, amount)

    def dp (self, idx, remAmount):
        if (idx, remAmount) in self.cache:
            return self.cache[(idx, remAmount)]
        if remAmount < 0 or idx == len(self.coins):
            return 0

        if remAmount == 0:
            return 1

        count = self.dp(idx + 1, remAmount)
        count += self.dp(idx, remAmount - self.coins[idx])
        self.cache[(idx, remAmount)] = count
        return count
        