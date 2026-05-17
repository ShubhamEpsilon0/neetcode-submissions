import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a > 0:
            maxHeap.append((-a, "a"))
        if b > 0:
            maxHeap.append((-b, "b"))
        if c > 0:
            maxHeap.append((-c, "c"))
        heapq.heapify(maxHeap)

        ans = ""
        prevChar = ""
        repeatCount = 0
        waitingItem = None

        while maxHeap:
            item = heapq.heappop(maxHeap)
            if item[1] == prevChar:
                repeatCount += 1
            else:
                repeatCount = 0
            prevChar = item[1]
            ans += item[1]

            if waitingItem:
                heapq.heappush(maxHeap, waitingItem)
                waitingItem = None

            if item[0] == -1:
                repeatCount = 0
                prevChar = ""
                continue
            
            if repeatCount == 1:
                waitingItem = (item[0] + 1, item[1])
            else:
                heapq.heappush(maxHeap, (item[0] + 1, item[1]))

        return ans



        