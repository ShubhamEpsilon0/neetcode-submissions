class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        targetSum = threshold * k
        R = k
        ans = 0
        curSum = sum(arr[:k])
        if curSum >= targetSum:
            ans += 1

        while R < len(arr):
            curSum = curSum + arr[R] - arr[R - k]
            if curSum >= targetSum:
                ans += 1
            R += 1

        return ans



        