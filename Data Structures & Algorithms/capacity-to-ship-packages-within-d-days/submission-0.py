class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        self.days = days
        
        leastWeight = max(self.weights)
        maxWeight = sum(self.weights)

        while leastWeight < maxWeight:
            mid = (leastWeight + maxWeight) // 2

            if self.IsShipWeightEnough(mid):
                maxWeight = mid
            else:
                leastWeight = mid + 1

        return maxWeight

    def IsShipWeightEnough(self, shipWeight):
        dayCount = 0
        curDayWeight = 0 
        for packageWeight in self.weights:
            if curDayWeight + packageWeight > shipWeight:
                 dayCount += 1
                 curDayWeight = 0
            curDayWeight += packageWeight

        return dayCount < self.days
            





        