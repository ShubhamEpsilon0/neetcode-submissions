from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if n == 1:
            return 0
        adjList = defaultdict(list)
        dp = [float("INF")] * n
        dp[dst] = 0

        for flight in flights:
            adjList[flight[0]].append((flight[1], flight[2]))
            if flight[1] == dst:
                dp[flight[0]] = flight[2]

        while k > 0:
            k -= 1
            new_dp = list(dp)
            for i in range(n):
                for neighbor in adjList[i]:
                    new_dp[i] = min(new_dp[i], neighbor[1] + dp[neighbor[0]])

            dp = new_dp

        return dp[src] if dp[src] != float("INF") else -1
        