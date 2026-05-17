class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        self.maxStack = []
        self.maxIndex = 0
        ans = []
        #prepare initial window 
        for n in nums[:k]:
            self.PushToStack(n)

        #start Finding max for each window
        for step in range(len(nums) - k + 1):
            ans.append(self.maxStack[self.maxIndex])

            #move the window
            if self.maxStack[self.maxIndex] == nums[step]:
                self.maxIndex += 1
            
            if step + k < len(nums):
                self.PushToStack(nums[step + k])

        return ans

    def PushToStack (self, num):
        while len(self.maxStack) > self.maxIndex and self.maxStack[-1] < num:
            self.maxStack.pop()

        self.maxStack.append(num)

        