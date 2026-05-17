"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        newBeginNode = Node(node.val)
        clonedNodesMap = {
            node.val: newBeginNode
        }
        queue = deque()
        queue.append(node)

        while queue:
            numElems = len(queue)
            for _ in range(numElems):
                curNode = queue.popleft()

                # Get clone node
                clonedNode = clonedNodesMap[curNode.val]

                # Create new neighbors if necessory and 
                # add original neighbors to queue if not visited
                for neighbor in curNode.neighbors:
                    if neighbor.val not in clonedNodesMap:
                        clonedNodesMap[neighbor.val] = Node(neighbor.val)
                        queue.append(neighbor)

                    clonedNode.neighbors.append(clonedNodesMap[neighbor.val])

        return newBeginNode

                    




        