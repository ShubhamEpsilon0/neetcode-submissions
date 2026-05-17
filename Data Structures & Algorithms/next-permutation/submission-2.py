class Solution:
    def reverse (self, nums, length, start):
        for i in range(length // 2):
            nums[start + i], nums[start + length - i - 1] = nums[start + length - i - 1], nums[start + i]

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            self.reverse(nums, n, 0)
            return

        # swap index = i - 1
        swapIndex = i
        for j in range(i, n):
            if nums[j] > nums[i - 1] and nums[swapIndex] > nums[j]:
                swapIndex = j
        
        nums[i - 1], nums[swapIndex] = nums[swapIndex], nums[i - 1]
        
        self.reverse(nums, n - i, i)
        