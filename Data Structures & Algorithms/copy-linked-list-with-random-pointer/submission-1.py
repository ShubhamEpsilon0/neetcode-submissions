"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        self.constructNodeMapping(head)
        newHead = self.nodeMap[head]

        while head:
            mappedNode = self.nodeMap[head]
            if head.random:
                mappedNode.random = self.nodeMap[head.random]

            head = head.next

        return newHead

    def constructNodeMapping(self, head):
        self.nodeMap = {}
        prev = None
        
        while head:
            newNode = Node(head.val)
            self.nodeMap[head] = newNode
            if prev:
                prev.next = newNode

            prev = newNode
            head = head.next
        