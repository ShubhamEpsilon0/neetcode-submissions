import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visitedNodesHeap = [(grid[0][0], 0,0)]
        visited = set()

        while visitedNodesHeap:
            d, r, c = heapq.heappop(visitedNodesHeap)

            if r == n - 1 and c == n - 1:
                return d

            visited.add((r,c))

            dirs=[(1,0), (-1,0), (0, 1), (0, -1)]

            for dir in dirs:
                if 0 <= r + dir[0] < n and 0 <= c + dir[1] < n and (r+dir[0], c+dir[1]) not in visited:
                    heapq.heappush(visitedNodesHeap, (max(d, grid[r+dir[0]][c+dir[1]]), r+dir[0], c+dir[1]))


        
        
                
                
        