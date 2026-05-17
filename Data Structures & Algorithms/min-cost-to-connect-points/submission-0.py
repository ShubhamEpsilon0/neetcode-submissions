class UnionFind:
    def __init__ (self, n):
        self.parent = list(range(n))

    def find(self, i):
        if i == self.parent[i]:
            return i

        return self.find(self.parent[i])

    def union(self, i, j):
        i_parent = self.find(i)
        j_parent = self.find(j)

        if i_parent == j_parent:
            return False
        self.parent[i_parent] = j_parent
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = self.enumerateEdges(points)
        n = len(points)
        uf = UnionFind(n)
        edges.sort()
        ans = 0
        edgesAdded = 0
        for edge in edges:
            if uf.union(edge[1], edge[2]):
                ans += edge[0]
                edgesAdded+=1

            if edgesAdded == n - 1:
                break

        return ans


    def enumerateEdges(self, nodes):
        edges = []

        def manhattanDistance (node1, node2): 
            return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

        for index1, node1 in enumerate(nodes):
            for index2, node2 in enumerate(nodes):
                if index1 == index2:
                    continue
                edges.append((manhattanDistance(node1, node2), index1, index2))

        return edges

        