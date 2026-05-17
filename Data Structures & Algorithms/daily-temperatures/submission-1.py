class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(101, -1)]
        ans = []
        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            while stack[-1][0] <= t:
                stack.pop()

            ans.insert(0, max(0, stack[-1][1] - i))
            stack.append((t, i))

        return ans

        