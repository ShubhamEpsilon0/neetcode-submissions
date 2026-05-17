import heapq
from collections import Counter, deque
class Solution:
    # max((maxFreq - 1) * (n + 1) + countMax, len(tasks))
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [(-count, task) for task, count in Counter(tasks).items()]
        heapq.heapify(maxHeap)
        coolDownQueue = deque()

        minCPUCycles = 0

        while maxHeap or coolDownQueue:
            minCPUCycles += 1
            if maxHeap:
                negCount, task = heapq.heappop(maxHeap)
                if negCount != -1:
                    coolDownQueue.append((minCPUCycles + n, (negCount + 1, task)))
            else:
                #Jump Ahead
                minCPUCycles = coolDownQueue[0][0]

            while coolDownQueue and coolDownQueue[0][0] <= minCPUCycles:
                cooledOffTask = coolDownQueue.popleft()[1]
                heapq.heappush(maxHeap, cooledOffTask)

        return minCPUCycles