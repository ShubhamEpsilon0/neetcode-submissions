class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        start = 0
        curSum = 0
        res = float('inf')
        for end in range(len(nums)):
            curSum += nums[end]

            while start < end and curSum - nums[start] >= target:
                curSum -= nums[start]
                start += 1

            if curSum >= target:
                res = min(res, end - start + 1)


        return res if res != float('inf') else 0
        