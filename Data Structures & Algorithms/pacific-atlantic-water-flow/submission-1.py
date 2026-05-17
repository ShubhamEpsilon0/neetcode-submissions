class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        for i in range(rows):
            dfs(i, 0, pac)
            dfs(i, cols - 1, atl)

        for j in range(cols):
            dfs(0, j, pac)
            dfs(rows - 1, j, atl)

        return list(pac & atl)
