import math
class Solution:
    def checkAnswerCorrectness(self, piles, ans, target):
        if ans == 0:
            return False
        time = 0
        for pile in piles:
            time += math.ceil(pile / ans)
        return time <= target

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            midWorks = self.checkAnswerCorrectness(piles, mid, h)
            midNeg1Works = self.checkAnswerCorrectness(piles, mid - 1, h)

            # check if mid is answer
            if midWorks and not midNeg1Works:
                return mid
            elif not midWorks:
                low = mid + 1
            else:
                high = mid - 1

        return -1
        