import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = [(val, index) for index, val in enumerate(queries)]
        queries.sort()

        minHeap = []
        i = 0
        res = [0]*len(queries)

        for query, index in queries:

            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i+=1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            if not minHeap:
                res[index] = -1
            else:
                res[index] =  minHeap[0][0]

        return res

            


        