from enum import Enum

class IntervalTimes:
    Start = 0
    End = 1

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[IntervalTimes.End])
        self.lastIncludedInterval = None
        count = 0
        for interval in intervals:
            if self.isNonOverlapping(interval):
                self.lastIncludedInterval = interval
                count += 1

        return len(intervals) - count
    

    def isNonOverlapping(self, interval):
        return (not self.lastIncludedInterval) or self.lastIncludedInterval[IntervalTimes.End] <= interval[IntervalTimes.Start]

        