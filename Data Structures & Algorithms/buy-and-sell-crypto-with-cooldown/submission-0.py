class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.cache = {}
        self.prices = prices
        self.pricesLen = len(self.prices)
        return self.dp(0, -1)

    def dp (self, index, buyIndex):
        if index >= self.pricesLen:
            return 0

        if ((index, buyIndex) in self.cache):
            return self.cache[(index, buyIndex)]

        if buyIndex >= 0:
            #Two Options Sell or keep holding
            curProfit = max(0, self.prices[index] - self.prices[buyIndex])
            self.cache[(index, buyIndex)] = max(
                self.dp(index + 1, buyIndex),
                (curProfit + self.dp(index + 2, -1)) if curProfit else 0
            )
        else:
            #Two Options buy or skip day
            self.cache[(index, buyIndex)] = max(
                self.dp(index + 1, -1),
                self.dp(index + 1, index),
            )
        return self.cache[(index, buyIndex)]
        