class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        self.nums = nums[:-1]
        self.cache = {}
        ans = self.dp(0)
        self.nums = nums[1:]
        self.cache = {}
        return max(ans, self.dp(0))

    def dp(self, curIndex):
        if curIndex >= len(self.nums):
            return 0

        if curIndex in self.cache:
            return self.cache[curIndex]

        self.cache[curIndex] = max(
            self.nums[curIndex] + self.dp(curIndex + 2),
            self.dp(curIndex + 1)
        ) 

        return self.cache[curIndex]

        
        