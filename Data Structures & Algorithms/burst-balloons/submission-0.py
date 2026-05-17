class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        self.nums = [1] + nums + [1]
        self.cache = {}

        L = 1
        R = len(self.nums) - 2

        return self.dp(L, R)


    def dp (self, L, R):
        if L > R:
            return 0

        if (L,R) in self.cache:
            return self.cache[(L,R)]

        self.cache[(L,R)] = 0
        for i in range(L, R + 1):
            # delete i last
            coins = self.nums[L-1] * self.nums[i] * self.nums[R+1]
            coins += self.dp(L, i - 1) + self.dp(i + 1, R)
            self.cache[(L,R)] = max(
                self.cache[(L,R)],
                coins
            )
        return self.cache[(L,R)]


        


        