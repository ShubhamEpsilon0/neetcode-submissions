from collections import defaultdict

class SubSetsMetaData:
    def __init__(self, subsetElems = [], count = 0):
        self.subset = list(subsetElems)
        self.count = count


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        divisible_subsets_map = defaultdict(SubSetsMetaData)
        nums.sort()
        for num in nums:
            divisible_subsets_map[num].subset = [num]
            divisible_subsets_map[num].count = 1

        n = len(nums)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    subset = SubSetsMetaData(
                        [nums[i], *(divisible_subsets_map[nums[j]].subset)],
                        divisible_subsets_map[nums[j]].count + 1
                    )
                    if subset.count > divisible_subsets_map[nums[i]].count:
                        divisible_subsets_map[nums[i]] = subset
        
        largest_subset = divisible_subsets_map[nums[0]]
        for subset in divisible_subsets_map.values():
            if subset.count > largest_subset.count:
                largest_subset = subset

        return largest_subset.subset

                    
                


        