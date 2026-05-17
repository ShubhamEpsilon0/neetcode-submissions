from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixArr = [0]
        for num in nums:
            prefixArr.append(prefixArr[-1] + num)

        seenCount = defaultdict(int)
        count = 0
        for num in prefixArr:
            if num - k in seenCount.keys():
                count += seenCount[num - k]
            seenCount[num] += 1

        return count
            
        