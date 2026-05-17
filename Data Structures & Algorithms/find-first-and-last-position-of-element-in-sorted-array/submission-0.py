class Solution:

    def binSearchLeft(self, nums, target):

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                return mid
            elif nums[mid] >= target:
                high = mid - 1
            else: 
                low = mid + 1

        return -1

    def binSearchRight(self, nums, target):

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2 
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
                return mid
            elif nums[mid] <= target:
                low = mid + 1
            else: 
                high = mid - 1

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.binSearchLeft(nums, target),
            self.binSearchRight(nums, target)
        ]
        