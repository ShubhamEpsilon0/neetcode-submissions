from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.preReqList = defaultdict(set)
        inorderCounter = defaultdict(int)
        adj = defaultdict(list)
        for preReq in prerequisites:
            adj[preReq[0]].append(preReq[1])
            inorderCounter[preReq[1]] += 1

        zeroInorderQueue = [node for node in range(numCourses) if inorderCounter[node] == 0]

        while zeroInorderQueue:
            node = zeroInorderQueue.pop()
            for neighbor in adj[node]:
                self.preReqList[neighbor].add(node)
                self.preReqList[neighbor] = self.preReqList[neighbor].union(self.preReqList[node])
                inorderCounter[neighbor] -= 1
                if inorderCounter[neighbor] == 0:
                    zeroInorderQueue.append(neighbor)

        return [query[0] in self.preReqList[query[1]] for query in queries]


        




        