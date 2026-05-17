class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        if n == 4:
            return [nums] if sum(nums) == target else []
        
        self.nums = nums
        self.numsLen = n
        self.nums.sort()

        self.result = set()
        self.findNextElems(0, 4, target, [])
        return list(self.result)


    def findNextElems (self, startIndex, numElems, remainingTarget, curCombination):
        if startIndex > self.numsLen - numElems:
            return

        if numElems == 2:
            res = self.Get2Sum(startIndex, self.numsLen - 1, remainingTarget)
            for pair in res:
                # print([*curCombination, *pair])
                self.result.add(tuple([*curCombination, *pair]))
            return

        curCombination.append(self.nums[startIndex])
        self.findNextElems(startIndex + 1, numElems - 1, remainingTarget - self.nums[startIndex], curCombination)
        curCombination.pop()

        self.findNextElems(startIndex + 1, numElems, remainingTarget, curCombination)

    def Get2Sum(self, l, r, target):
        res = set()
        while l < r:
            if self.nums[l] + self.nums[r] == target:
                res.add((self.nums[l], self.nums[r]))
                l += 1
                r -= 1
            elif self.nums[l] + self.nums[r] > target:
                r -= 1
            else:
                l += 1

        return res
