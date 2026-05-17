# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import json
class Codec:    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree = self.dictifyTree(root)
        return json.dumps(tree)

    def dictifyTree(self, root):
        if not root:
            return None
        return {
            root.val: {
                "L" : self.serialize(root.left),
                "R": self.serialize(root.right)
            }
        }
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data == 'null':
            return None
        
        tree = json.loads(data)
        root = TreeNode(list(tree.keys())[0])
        root.left = self.deserialize(tree[root.val]["L"])
        root.right = self.deserialize(tree[root.val]["R"])

        return root

        
