from collections import Counter
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] -= 1 #negative count for minHeap

        freqMapItems =[(negCount,num) for num, negCount in freqMap.items()]
        heapq.heapify(freqMapItems)
        ans = []
        while k > 0:
            negCount,num = heapq.heappop(freqMapItems)
            ans.append(num)
            k-=1

        return ans


        

        