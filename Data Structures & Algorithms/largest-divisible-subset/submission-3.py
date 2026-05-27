from collections import defaultdict

class SubSetsMetaData:
    def __init__(self, elem = None, nextNum = None, totalCount = 0):
        self.elem = elem
        self.nextNum = nextNum
        self.totalCount = totalCount


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums

        divisible_subsets_map = defaultdict(SubSetsMetaData)
        nums.sort()
        for num in nums:
            divisible_subsets_map[num].elem = num
            divisible_subsets_map[num].totalCount = 1

        
        largest_subset = divisible_subsets_map[nums[0]]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    subset = SubSetsMetaData(
                        nums[i],
                        nums[j],
                        divisible_subsets_map[nums[j]].totalCount + 1
                    )
                    if subset.totalCount > divisible_subsets_map[nums[i]].totalCount:
                        divisible_subsets_map[nums[i]] = subset
                        if subset.totalCount > largest_subset.totalCount:
                            largest_subset = subset
        
        largest_subset_list = []
        while largest_subset.nextNum is not None:
            largest_subset_list.append(largest_subset.elem)
            largest_subset = divisible_subsets_map[largest_subset.nextNum]

        largest_subset_list.append(largest_subset.elem)

        return largest_subset_list

                    
                


        