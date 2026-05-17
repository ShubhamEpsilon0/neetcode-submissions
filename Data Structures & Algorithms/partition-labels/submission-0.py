from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freqMap = Counter(s)
        curMap = set()
        curLen = 0
        curMapValuesSum = 0
        ans= []

        for ch in s:
            if ch in curMap:
                curMapValuesSum -= 1
            else:
                curMap.add(ch)
                curMapValuesSum += freqMap[ch] - 1

            curLen += 1

            if curMapValuesSum == 0:
                curMap = set()
                ans.append(curLen)
                curLen = 0


        return ans

        