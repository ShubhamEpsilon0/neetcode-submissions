class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])


        visit = set()
        curPath = set()
        topSort = []
        for i in range(numCourses) :
            if not self.dfs(i, adj, visit, curPath, topSort):
                return []

        return topSort

    def dfs(self, src, adj, visit, curPath, topSort):
        if src in curPath:
            return False

        if src in visit:
            return True

        visit.add(src)
        curPath.add(src)

        for neightbor in adj[src]:
            if not self.dfs(neightbor, adj, visit, curPath, topSort):
                return False

        curPath.remove(src)
        topSort.append(src)
        return True

        
        