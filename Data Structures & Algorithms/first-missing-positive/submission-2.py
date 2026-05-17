class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        i = 0
        n = len(nums)

        if (sum(nums) == (n * (n + 1))// 2):
            return n + 1

        while i < n:
            if nums[i] <= 0 or nums[i] == i:
                i += 1
                continue

            # Try to Swap
            if nums[i] >= n or nums[i] == nums[nums[i]]:
                nums[i] = -1
                i += 1
                continue

            temp = nums[nums[i]]
            nums[nums[i]] = nums[i]
            nums[i] = temp
            

        for i in range(1, n):
            if i != nums[i]:
                return i

        return n
        