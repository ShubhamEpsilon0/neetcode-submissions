class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        low = 0
        high = len(nums1) - 1

        totalNumElems = len(nums1) + len(nums2)
        size_first_half = (totalNumElems) // 2

        while True:
            mid1 = (low + high) // 2
            mid2 = size_first_half - mid1 - 2

            nums1Left = nums1[mid1] if mid1 >= 0 else float("-INF")
            nums2Left = nums2[mid2] if mid2 >= 0 else float("-INF")

            nums1Right = nums1[mid1 + 1] if (mid1 + 1) < len(nums1) else float("INF")
            nums2Right = nums2[mid2 + 1] if (mid2+1) < len(nums2) else float("INF")

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if  totalNumElems % 2 == 0:
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
                else:
                    return min(nums1Right, nums2Right)
            elif nums1Left > nums2Right:
                high = mid1 - 1
            else:
                low = mid1 + 1
                
        
        