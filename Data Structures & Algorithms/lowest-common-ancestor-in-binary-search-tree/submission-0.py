# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.LCA(root, min(p.val, q.val), max(p.val, q.val))

    def LCA(self, root, minVal, maxVal):
        if root.val >= minVal and root.val <= maxVal:
            return root

        if root.val > maxVal:
            return self.LCA(root.left, minVal, maxVal)
        else:
            return self.LCA(root.right, minVal, maxVal)
