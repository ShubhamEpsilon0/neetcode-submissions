class UnionFind:
    def __init__(self, n):
        self. n = n
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i

        return self.find(self.parent[i])

    def union (self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u != parent_v:
            self.parent[parent_u] = parent_v
            return True

        return False
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        ans = n
        for edge in edges:
            if uf.union(edge[0], edge[1]):
                ans -= 1

        return ans
        