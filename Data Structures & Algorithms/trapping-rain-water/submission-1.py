class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]
        ans = 0
        prevMax = height[0]

        for i in range(1, len(height) - 1):
            prevMax = max(prevMax, height[i-1])
            leftMax.append(prevMax)
        leftMax.append(0)

        prevMax= height[-1]

        for i in range(len(height) - 2, 0, -1):
            prevMax = max(prevMax, height[i+1])
            ans += max(
                0, min(leftMax[i],prevMax) - height[i]
            )

        return ans

        