class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.coins.sort()
        self.cache = {}
        
        ans = self.dp(len(coins) - 1, amount)

        return ans if ans != float("inf") else -1


    def dp (self, index, remAmount):
        if (index, remAmount) in self.cache:
            return self.cache[(index, remAmount)]
        if remAmount == 0:
            return 0

        if remAmount < 0:
            return float("inf")
        if index < 0:
            return float("inf")

        self.cache[(index, remAmount)] = min(
            1 + self.dp(index, remAmount - self.coins[index]),
            self.dp(index - 1, remAmount)
        )
        
        return self.cache[(index, remAmount)]
        
        

        

        
        

        