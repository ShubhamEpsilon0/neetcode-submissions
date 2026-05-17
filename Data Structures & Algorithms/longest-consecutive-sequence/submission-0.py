class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0
        
        for num in nums:
            if num - 1 in numSet:
                continue
            else:
                count = 1
                num1 = num
                while num1 + 1 in numSet:
                    count += 1
                    num1 += 1
                maxCount = max(maxCount, count)

        return maxCount
        