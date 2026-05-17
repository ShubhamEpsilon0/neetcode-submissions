from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqMap = Counter(hand)
        uniqueKeys = list(freqMap.keys())
        uniqueKeys.sort(reverse=True)

        while uniqueKeys:
            start = uniqueKeys.pop()
            if freqMap[start] == 0:
                continue
            startFreq = freqMap[start]
            for i in range(start, start + groupSize):
                if freqMap[i] < startFreq:
                    return False
                freqMap[i] -= startFreq

        return True

        