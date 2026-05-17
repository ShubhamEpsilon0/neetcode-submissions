class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curBuyIndex = 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                profit += max(0, prices[i-1] - prices[curBuyIndex])
                curBuyIndex = i
        
        if curBuyIndex != len(prices):
            profit+=max(0, prices[-1] - prices[curBuyIndex])

        return profit

        