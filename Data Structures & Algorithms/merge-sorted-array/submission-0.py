class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #shift nums1 towards the end
        for i in range(m + n - 1, n - 1, -1):
            nums1[i] = nums1[i - n]

        newPtr = 0
        nPtr = 0
        newMPtr = n

        while nPtr < n and newMPtr < m + n:
            if nums1[newMPtr] < nums2[nPtr]:
                nums1[newPtr] = nums1[newMPtr]
                newPtr += 1
                newMPtr += 1
            else:
                nums1[newPtr] = nums2[nPtr]
                newPtr += 1
                nPtr += 1

        while nPtr < n:
            nums1[newPtr] = nums2[nPtr]
            newPtr += 1
            nPtr += 1


