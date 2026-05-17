# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.preorder = preorder

        self.inorderNodeMap = {}
        for index, node in enumerate(inorder):
            self.inorderNodeMap[node] = index

        return self.buildTreeRecur(0, len(inorder) - 1)


    def buildTreeRecur(self, inOrderStart, inOrderEnd):
        if not self.preorder:
            return None

        if inOrderStart < 0 or inOrderEnd >= len(self.inorder) or inOrderEnd < inOrderStart:
            return None

        root = TreeNode(self.preorder.pop(0))
        root.left = self.buildTreeRecur(inOrderStart, self.inorderNodeMap[root.val] - 1)
        root.right = self.buildTreeRecur(self.inorderNodeMap[root.val] + 1, inOrderEnd)

        return root
        
        