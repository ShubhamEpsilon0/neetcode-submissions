class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        minOps = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                minOps += target[i] - target[i - 1]

        return minOps
        