class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(startIndex, Height)
        maxArea = 0
        for index, height in enumerate(heights):
            lastPoppedIndex = index
            while stack and stack[-1][1] > height:
                poppedElem = stack.pop()
                maxArea = max(maxArea, (index - poppedElem[0]) * poppedElem[1])
                lastPoppedIndex = poppedElem[0]
            
            stack.append((lastPoppedIndex, height))

        n = len(heights)
        while stack:
            poppedElem = stack.pop()
            maxArea = max(maxArea, (n - poppedElem[0]) * poppedElem[1])

        return maxArea


        