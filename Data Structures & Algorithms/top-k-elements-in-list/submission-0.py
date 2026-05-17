from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        buckets = []

        for _ in range((max(set(freqMap.values())) + 1)):
            buckets.append([])

        for num, freq in freqMap.items():
            buckets[freq].append(num)

        ans = []
        curBucketIndex = len(buckets) - 1
        while k > 0 and curBucketIndex >= 0:
            elemCount = len(buckets[curBucketIndex])
            if elemCount:
                ans.extend(buckets[curBucketIndex])
                k -= elemCount
            curBucketIndex -= 1

        return ans

        