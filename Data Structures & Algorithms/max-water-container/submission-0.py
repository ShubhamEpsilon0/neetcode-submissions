class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            maxArea = max(maxArea, min(heights[L], heights[R]) * (R - L))
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1

        return maxArea

        