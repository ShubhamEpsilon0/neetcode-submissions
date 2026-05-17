class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = [1]
        suffixProd = [1]
        prod = 1
        for num in nums[:-1]:
            prod *= num
            prefixProd.append(prod)
        prod = 1
        for num in nums[::-1][:-1]:
            prod*= num
            suffixProd.insert(0, prod)
        ans = []
        for i in range(len(nums)):
            ans.append(prefixProd[i] * suffixProd[i])
        return ans

        