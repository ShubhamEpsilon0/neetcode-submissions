class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                if target == nums[l] + nums[r]:
                    ans.add((nums[i], nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif target > nums[l] + nums[r]:
                    l += 1
                else:
                    r -= 1
        return list(ans)

        