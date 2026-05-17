class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diff = [(g - c) for g,c in zip(gas, cost)]
        total = 0
        index = 0
        for i, d in enumerate(diff):
            total += d
            if total < 0:
                index = i + 1
                total = 0

        return index
        