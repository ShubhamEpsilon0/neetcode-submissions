"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        numDays = 0
        heap = []
        for interval in intervals:
            if heap and heap[0] <= interval.start: #compatible with some day
                heapq.heappop(heap)
            else:
                numDays += 1
            
            heapq.heappush(heap, interval.end)

        return numDays
        