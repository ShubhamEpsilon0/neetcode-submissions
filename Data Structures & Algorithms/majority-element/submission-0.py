class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stack = []

        for num in nums:
            if stack and stack[-1] != num:
                stack.pop()
            else:
                stack.append(num)
        
        return stack[-1]