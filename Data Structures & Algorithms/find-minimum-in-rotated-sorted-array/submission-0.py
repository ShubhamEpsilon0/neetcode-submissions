class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Not rotated or rotated back to original state
        if nums[0] <= nums[-1]:
            return nums[0]


        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if mid != 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[-1]:
                low = mid + 1
            else:
                high = mid - 1

        return -1         
        