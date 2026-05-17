class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        smallestPossiblePathOnRight = n - 1
        print(smallestPossiblePathOnRight)
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= smallestPossiblePathOnRight:
                smallestPossiblePathOnRight = i
                print(smallestPossiblePathOnRight)

        return smallestPossiblePathOnRight == 0
        