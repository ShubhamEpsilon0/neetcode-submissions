from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        
        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])


        visit = set()
        curPath = set()
        for i in range(numCourses) :
            if not self.dfs(i, adj, visit, curPath):
                return False

        return True

    def dfs(self, src, adj, visit, curPath):
        if src in curPath:
            return False

        if src in visit:
            return True

        visit.add(src)
        curPath.add(src)

        for neightbor in adj[src]:
            if not self.dfs(neightbor, adj, visit, curPath):
                return False

        curPath.remove(src)
        return True

        