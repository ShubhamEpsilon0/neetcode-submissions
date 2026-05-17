from enum import Enum

class NextOp(Enum):
    ANYTHING = 1
    GREATER = 2
    LESSER = 4


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxCount = 1
        curCount = 1
        nextOp = NextOp.ANYTHING
        i = 1
        while i < len(arr):
            if (arr[i] > arr[i - 1]) and (nextOp == NextOp.ANYTHING or nextOp == NextOp.GREATER):
                curCount += 1
                nextOp = NextOp.LESSER
            elif (arr[i] < arr[i - 1]) and (nextOp == NextOp.ANYTHING or nextOp == NextOp.LESSER):
                curCount += 1
                nextOp = NextOp.GREATER
            else:
                maxCount = max(maxCount, curCount)
                curCount = 1
                if arr[i] != arr[i-1]:
                    i -= 1
                nextOp = NextOp.ANYTHING

            i += 1

        return max(maxCount, curCount)
