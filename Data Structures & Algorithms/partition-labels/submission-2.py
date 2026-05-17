from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freqMap = Counter(s)
        curLen = 0
        curMapValuesSum = 0
        ans= []

        for ch in s:
            if freqMap[ch] > 0:
                curMapValuesSum += freqMap[ch]
                freqMap[ch] = 0

            curMapValuesSum -= 1
            curLen += 1

            if curMapValuesSum == 0:
                ans.append(curLen)
                curLen = 0


        return ans

        