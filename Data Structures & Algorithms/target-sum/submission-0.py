class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.numsLen = len(nums)
        self.target = target
        self.cache = {}

        return self.dp(0, 0)


    def dp (self, index, curSum):
        if (index, curSum) in self.cache:
            return self.cache[(index, curSum)]

        if index == self.numsLen:
            if curSum == self.target:
                return 1
            return 0

        numWays = 0

        numWays += self.dp(index + 1, curSum + self.nums[index])
        numWays += self.dp(index + 1, curSum - self.nums[index])

        self.cache[(index, curSum)] = numWays

        return numWays

        

        
        