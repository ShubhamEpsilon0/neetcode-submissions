from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        for n in nums:
            prefixSum.append(n + prefixSum[-1])

        seenSum = defaultdict(int)

        count = 0
        for s in prefixSum:
            if s - k in seenSum.keys():
                count += seenSum[s - k]
            seenSum[s] += 1

        return count

            
        