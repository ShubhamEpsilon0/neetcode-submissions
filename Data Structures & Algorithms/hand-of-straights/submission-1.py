from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqMap = Counter(hand)
        uniqueKeys = list(freqMap.keys())
        uniqueKeys.sort(reverse=True)

        while uniqueKeys:
            start = uniqueKeys.pop()
            while freqMap[start]:
                for i in range(start, start + groupSize):
                    if freqMap[i] == 0:
                        return False
                    freqMap[i] -= 1

        return True

        