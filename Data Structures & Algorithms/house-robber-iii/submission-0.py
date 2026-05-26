# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.cache = {}
        return self.dp(root)

    def dp(self, curNode):
        if curNode in self.cache:
            return self.cache[curNode]

        if curNode is None:
            return 0

        if curNode.left is None and curNode.right is None:
            return curNode.val
        
        max_rob_able_money = 0

        #Rob Current House
        grand_children = self.getGrandChildren(curNode)
        max_rob_able_money += curNode.val
        for grand_child in grand_children:
            max_rob_able_money += self.dp(grand_child)

        # Do Not rob current House
        max_rob_able_money = max(
            max_rob_able_money,
            self.dp(curNode.left) + self.dp(curNode.right)
        )

        self.cache[curNode] = max_rob_able_money

        return self.cache[curNode]


    def getGrandChildren(self, node):
        grand_children = []
        # left grand child
        if node.left:
            grand_children.extend([node.left.left, node.left.right])

        if node.right:
            grand_children.extend([node.right.left, node.right.right])

        return [node for node in grand_children if node is not None]


        