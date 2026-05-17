import heapq
import math
from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if (k == len(arr)):
            return arr
        
        heap = [(abs(x - num), num) for num in arr]
        heapq.heapify(heap)

        result = deque ()
        while k > 0:
            _, elem = heapq.heappop(heap)
            if elem >= x:
                result.append(elem)
            else:
                result.appendleft(elem)
            k -= 1

        return list(result)