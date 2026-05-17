# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.curVal = -1000000
        self.Result = True

        self.inOrderTraversal(root)
        return self.Result

    def processRoot(self, val):
        if self.curVal < val:
            self.curVal = val
        else:
            self.Result = False 

    def inOrderTraversal (self, root):
        if not root:
            return

        self.inOrderTraversal(root.left)
        self.processRoot(root.val)
        self.inOrderTraversal(root.right)



        



        

        