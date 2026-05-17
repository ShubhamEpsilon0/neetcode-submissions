class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        self.maxStack = []
        ans = []
        #prepare initial window 
        for n in nums[:k]:
            self.PushToStack(n)

        #start Finding max for each window
        for step in range(len(nums) - k + 1):
            ans.append(self.maxStack[0])

            #move the window
            if self.maxStack[0] == nums[step]:
                self.maxStack.pop(0)
            
            if step + k < len(nums):
                self.PushToStack(nums[step + k])

        return ans

    def PushToStack (self, num):
        while self.maxStack and self.maxStack[-1] < num:
            self.maxStack.pop()

        self.maxStack.append(num)

        