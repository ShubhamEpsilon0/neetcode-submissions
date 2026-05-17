import heapq
class Solution:
    def addToHeap(self, curCapital):
        while self.zippedProfCapIndex and self.zippedProfCapIndex[0][0] <= curCapital:
            profCapIndexItem = self.zippedProfCapIndex.pop(0)
            heapq.heappush(self.profCapHeap, (profCapIndexItem[1], profCapIndexItem[0], profCapIndexItem[2]))

            
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        self.zippedProfCapIndex = []

        for i in range(len(profits)):
            self.zippedProfCapIndex.append((capital[i], -profits[i], i))

        self.zippedProfCapIndex.sort()

        self.profCapHeap = []
        self.addToHeap (w)
        i = 0
        while self.profCapHeap and i < k:
            poppedElem = heapq.heappop(self.profCapHeap)
            w += -poppedElem[0]
            i += 1
            self.addToHeap (w)

        return w



        
        