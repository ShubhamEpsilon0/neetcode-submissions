import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kLargestHeap = []
        self.heapSize = 0
        self.k = k

        for num in nums:
            self.add(num)

        

    def add(self, val: int) -> int:
        if self.heapSize < self.k:
            heapq.heappush(self.kLargestHeap, val)
            self.heapSize+=1

        elif self.kLargestHeap[0] < val:
            heapq.heappop(self.kLargestHeap)
            heapq.heappush(self.kLargestHeap, val)

        return self.kLargestHeap[0]

        
