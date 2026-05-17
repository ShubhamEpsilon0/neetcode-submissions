class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        if nums[0] > nums[-1]:
            #Find Rotated Half
            startIndex = self.searchStartIndex(nums)
            if startIndex == -1:
                return -2
            if target >= nums[0]:
                end = startIndex - 1
            else:
                start = startIndex

        # Not Rotated
        #Perform BinSearch Directly
        print(start, end)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def searchStartIndex (self, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if mid !=0 and nums[mid - 1] > nums[mid]:
                return mid
            elif nums[mid] > nums[-1]:
                low = mid + 1
            else:
                high = mid - 1

        return -1