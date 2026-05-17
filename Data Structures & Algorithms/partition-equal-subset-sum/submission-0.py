class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        numSum = sum(nums)
        if numSum % 2 != 0:
            return False

        self.cache = {}
        self.nums = nums
        return self.bt(0, numSum // 2)

    def bt(self, index, targetSum):
        if (index, targetSum) in self.cache:
            return self.cache[(index, targetSum)]
        if targetSum == 0:
            return True

        if index == len(self.nums):
            return False

        self.cache[(index, targetSum)] = self.bt(index + 1, targetSum) or self.bt(index + 1, targetSum - self.nums[index])

        return self.cache[(index, targetSum)]
        