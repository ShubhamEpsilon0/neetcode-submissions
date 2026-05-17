import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = [float("INF")]*(n+1)
        d[0] = 0
        d[k] = 0

        adjList = defaultdict(list)
        for time in times:
            adjList[time[0]].append((time[2], time[1]))

        shortestEdgeHeap = [(0,k)]

        while shortestEdgeHeap:
            w, u = heapq.heappop(shortestEdgeHeap)

            if w > d[u]:
                continue
            
            for dist, node in adjList[u]:

                if d[node] > d[u] + dist:
                    d[node] = d[u] + dist
                    heapq.heappush(shortestEdgeHeap, (d[node], node))

        maxTime = max(d)
        print(d)
        return maxTime if maxTime != float("INF") else -1


        