class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(self.genPerms(0, nums))

    def genPerms (self, index, nums):
        if index == len(nums):
            return [[]]

        perms = self.genPerms(index + 1, nums)
        resPerms = set()

        for p in perms:
            for j in range(len(p) + 1):
                pCopy = list(p)
                pCopy.insert(j, nums[index])
                resPerms.add(tuple(pCopy))

        return resPerms


        