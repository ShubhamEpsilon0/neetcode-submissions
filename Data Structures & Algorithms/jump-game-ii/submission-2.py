class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        farthestReach = nums[0]
        n = len(nums)
        if n == 1:
            return 0
        count = 1
        
        while farthestReach < n - 1:
            l = r + 1
            r = farthestReach
            farthestReach = l + nums[l]
            count += 1
            while l <= r:
                farthestReach = max(farthestReach, l + nums[l])
                l += 1
        return count

        

        