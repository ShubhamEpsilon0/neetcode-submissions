class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0]
        stack = [heights[-1]]

        for i in range(n - 2, -1, -1):
            removedCount = 0
            while stack and stack[-1] < heights[i]:
                removedCount += 1
                stack.pop()

            if stack:
                removedCount += 1

            stack.append(heights[i])

            ans.insert(0, removedCount)

        return ans
        