class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        num_envelops = len(envelopes)
        if num_envelops == 1:
            return 1
        envelopes.sort()
        dp = [1] * num_envelops
        for i in range(num_envelops - 2, -1, -1):
            for j in range(i + 1, num_envelops):
                if self.canBeRussianEnveloped(envelopes[i], envelopes[j]):
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

    def canBeRussianEnveloped(self, envelopDimensions1, envelopDimensions2):
        return envelopDimensions1[0] < envelopDimensions2[0] and envelopDimensions1[1] < envelopDimensions2[1]
        