class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        numSum = sum(nums)
        if numSum % 2 != 0:
            return False

        targetSum = numSum // 2

        dp = [False] * (targetSum + 1)
        dp[0] = True

        for num in nums:
            for s in range(targetSum, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[targetSum]