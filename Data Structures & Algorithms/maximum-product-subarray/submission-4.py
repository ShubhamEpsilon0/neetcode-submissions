class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negProd = 0
        curProd = 0
        maxProd = nums[0]

        for num in nums:
            if num > 0:
                curProd = max(1, curProd) * num
                negProd *= num
            elif num == 0:
                negProd = 0
                curProd = 0
            else:
                if negProd != 0:
                    temp = max(curProd, 1)
                    curProd = negProd * num
                    negProd = temp * num
                else:
                    negProd = max(1, curProd) * num
                    curProd = -float("INF")


            maxProd = max(maxProd, curProd)
        return maxProd



        