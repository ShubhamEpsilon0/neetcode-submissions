from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res = self.constructDependencyGraph(words)
        if res == None:
            return ""
        adjList, inOrderCounts = res

        zeroInorderNodes = []
        for node in adjList.keys():
            if inOrderCounts[node] == 0:
                zeroInorderNodes.append(node)
        order = ""
        while zeroInorderNodes:
            char = zeroInorderNodes.pop(0)
            order += char
            for neighbor in adjList[char]:
                inOrderCounts[neighbor] -= 1
                if inOrderCounts[neighbor] == 0:
                    zeroInorderNodes.append(neighbor)

        return order if len(order) == len(adjList.keys()) else ""

    def constructDependencyGraph (self, words):
        adjlist = {}
        inOrderCounts = defaultdict(int)

        for word in words:
            for char in word:
                adjlist[char] = []

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return None
                if words[i][j] != words[i + 1][j]:
                    adjlist[words[i][j]].append(words[i+1][j])
                    inOrderCounts[words[i+1][j]] += 1
                    break

        return adjlist, inOrderCounts
        