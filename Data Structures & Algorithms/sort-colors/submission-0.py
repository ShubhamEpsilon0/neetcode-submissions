from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        j = 0
        for i in [0, 1, 2]:
            count = c[i]
            while count > 0:
                nums[j] = i
                j += 1
                count -= 1
        