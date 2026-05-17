import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x**2+y**2, [x,y]) for x,y in points]
        heapq.heapify(heap)

        ans = []
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -=1
        return ans
        