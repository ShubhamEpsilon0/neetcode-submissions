class UnionFind:

    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if node == self.parents[node]:
            return node

        return self.find(self.parents[node])

    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)

        if parent_i == parent_j:
            return False
        else:
            if self.rank[parent_i] >  self.rank[parent_j]:
                self.parents[parent_j] = parent_i
            elif  self.rank[parent_j] > self.rank[parent_i]:
                self.parents[parent_i] = parent_j
            else:
                self.parents[parent_j] = parent_i
                self.rank[parent_i] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False

        uf = UnionFind(n)

        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                # if a cycle is found, then it's not a tree
                return False

        #if all components are not connected, it's not a tree..
        treeRoot = uf.find(0)
        for i in range(1, n):
            if uf.find(i) != treeRoot:
                return False
        return True


        