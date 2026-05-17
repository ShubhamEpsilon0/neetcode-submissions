# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.countGoodNodes(root, -101)
        return self.count

    def countGoodNodes(self, root, curMax):
        if not root:
            return
        if root.val >= curMax:
            curMax = root.val
            self.count += 1

        self.countGoodNodes(root.left, curMax)
        self.countGoodNodes(root.right, curMax)

        