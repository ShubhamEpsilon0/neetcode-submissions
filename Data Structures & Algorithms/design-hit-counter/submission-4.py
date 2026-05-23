class HitCounterQueueData:
    def __init__(self):
        self.lastRecordedTimestamp = None
        self.count = 0


class HitCounter:
    MAX_BUCKETS = 300

    def __init__(self):
        self.buckets = [HitCounterQueueData () for _ in range(HitCounter.MAX_BUCKETS)] 


    def computeBucketNumber(self, timestamp):
        return timestamp % HitCounter.MAX_BUCKETS
    
    def hit(self, timestamp: int) -> None:
        bucketNum = self.computeBucketNumber(timestamp)

        if self.buckets[bucketNum].lastRecordedTimestamp != timestamp:
            self.buckets[bucketNum].lastRecordedTimestamp = timestamp
            self.buckets[bucketNum].count = 0

        self.buckets[bucketNum].count += 1

    def getHits(self, timestamp: int) -> int:
        hits = 0
        timestamp_300_sec_old = timestamp - 300
        for i in range(HitCounter.MAX_BUCKETS):
            if self.buckets[i].lastRecordedTimestamp and self.buckets[i].lastRecordedTimestamp > timestamp_300_sec_old:
                hits += self.buckets[i].count
        return hits
        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
