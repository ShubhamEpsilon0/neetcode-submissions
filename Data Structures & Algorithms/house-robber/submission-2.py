class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n):
            newVal = max(dp[1], dp[0] + nums[i])
            dp[0] = dp[1]
            dp[1] = newVal

        return dp[-1]

        