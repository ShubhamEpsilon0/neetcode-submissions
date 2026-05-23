class HitCounter:
    MAX_QUEUE_SIZE = 300

    def __init__(self):
        self.fixedSizeCircularQueue = [0] * HitCounter.MAX_QUEUE_SIZE #max size = 300
        self.epochStartTimestamp = None
        self.startIndex = 0
        self.lastRecordedTimestamp = None

    def checkIfOverflowOccured (self, timestamp):
        return timestamp - self.epochStartTimestamp >= HitCounter.MAX_QUEUE_SIZE

    def resetStartIndexAndEpoch(self, timestamp): 
        if timestamp >= self.lastRecordedTimestamp + HitCounter.MAX_QUEUE_SIZE:
            # complete reset
            self.startIndex = 0
            self.epochStartTimestamp = timestamp
            self.fixedSizeCircularQueue = [0] * HitCounter.MAX_QUEUE_SIZE
        else:
            newStartIndex = (self.startIndex + (timestamp - (HitCounter.MAX_QUEUE_SIZE - 1) - self.epochStartTimestamp)) % HitCounter.MAX_QUEUE_SIZE
            for i in range(self.startIndex, newStartIndex):
                self.fixedSizeCircularQueue[i] = 0

            self.startIndex = newStartIndex
            self.epochStartTimestamp = timestamp - (HitCounter.MAX_QUEUE_SIZE - 1)

    def computeQueueIndex(self, timestamp):
        return (self.startIndex + timestamp - self.epochStartTimestamp) % HitCounter.MAX_QUEUE_SIZE

    def hit(self, timestamp: int) -> None:
        if not self.epochStartTimestamp:
            self.epochStartTimestamp = timestamp

        if self.checkIfOverflowOccured(timestamp):
            self.resetStartIndexAndEpoch(timestamp)

        self.fixedSizeCircularQueue[self.computeQueueIndex(timestamp)] += 1
        self.lastRecordedTimestamp = timestamp
        

    def getHits(self, timestamp: int) -> int:
        if self.checkIfOverflowOccured(timestamp):
            self.resetStartIndexAndEpoch(timestamp)
        
        startIndex = self.computeQueueIndex(timestamp - (HitCounter.MAX_QUEUE_SIZE - 1))
        endIndex = self.computeQueueIndex(self.lastRecordedTimestamp)
        
        if startIndex <= endIndex:
            return sum(self.fixedSizeCircularQueue[startIndex: endIndex + 1])
        else:
            return sum(self.fixedSizeCircularQueue[startIndex:] + self.fixedSizeCircularQueue[: endIndex + 1])


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
