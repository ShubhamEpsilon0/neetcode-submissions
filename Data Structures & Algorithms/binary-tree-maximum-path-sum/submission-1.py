# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalMax = -float("INF")
        rootMax = self.helper(root)
        return max(self.globalMax, rootMax)

    def helper (self, root):
        if not root:
            return 0

        leftMax = max(0, self.helper(root.left))
        rightMax = max(0, self.helper(root.right))

        # print(leftMax, rightMax)

        maxWithOnePath = max(leftMax, rightMax) + root.val
        totalWithBothPaths = leftMax+ rightMax + root.val
        # print(maxWithOnePath,totalWithBothPaths )
        self.globalMax = max(self.globalMax, maxWithOnePath, totalWithBothPaths)
        # print(self.globalMax)
        return maxWithOnePath
        