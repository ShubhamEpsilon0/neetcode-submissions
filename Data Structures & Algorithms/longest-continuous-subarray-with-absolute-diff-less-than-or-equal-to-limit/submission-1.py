class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longestSubArrLen = 1

        start = 0
        minQ = [nums[0]] + [float("INF")] * len(nums)
        maxQ = [nums[0]] + [-float("INF")] * len(nums)

        for end in range(1, len(nums)):
            
            #insert in minQ
            i = 0
            while minQ[i] <= nums[end]:
                i+= 1
            minQ[i] = nums[end]

            #insert in maxQ
            i = 0
            while maxQ[i] >= nums[end]:
                i+= 1
            maxQ[i] = nums[end]

            while start < end and abs(maxQ[0] - minQ[0]) > limit:
                if nums[start] == maxQ[0]:
                    maxQ.pop(0)
                if nums[start] == minQ[0]:
                    minQ.pop(0)
                start += 1

            longestSubArrLen = max(longestSubArrLen, end - start + 1)
        return longestSubArrLen

        