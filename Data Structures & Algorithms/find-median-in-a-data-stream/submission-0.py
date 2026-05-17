import heapq
class MedianFinder:

    def __init__(self):
        self.largeNumsMinHeap =[]
        self.smallNumsMaxHeap = []

    def checkComparativeInVariant(self):
        if not len(self.largeNumsMinHeap) or not len(self.smallNumsMaxHeap):
            return
        if -self.smallNumsMaxHeap[0] <= self.largeNumsMinHeap[0]:
            return
        heapq.heappush(self.largeNumsMinHeap, -heapq.heappop(self.smallNumsMaxHeap))


    def checkHeapSizeInVariant(self):
        if len(self.largeNumsMinHeap) - len(self.smallNumsMaxHeap) > 1:
            heapq.heappush(self.smallNumsMaxHeap, -heapq.heappop(self.largeNumsMinHeap))
        elif len(self.smallNumsMaxHeap) - len(self.largeNumsMinHeap) > 1:
            heapq.heappush(self.largeNumsMinHeap, -heapq.heappop(self.smallNumsMaxHeap))
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallNumsMaxHeap, -num)

        self.checkComparativeInVariant()
        self.checkHeapSizeInVariant()

    def findMedian(self) -> float:
        if len(self.largeNumsMinHeap) == len(self.smallNumsMaxHeap):
            return (self.largeNumsMinHeap[0] - self.smallNumsMaxHeap[0]) / 2
        elif len(self.largeNumsMinHeap) > len(self.smallNumsMaxHeap):
            return self.largeNumsMinHeap[0]
        else:
            return -self.smallNumsMaxHeap[0]


        
        