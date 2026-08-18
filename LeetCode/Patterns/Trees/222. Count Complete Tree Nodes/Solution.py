# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def Indo(node):
            if not node:
                return 0
            lh = Indo(node.left)
            rh = Indo(node.right)
            maxii = 1 + lh + rh
            return maxii
        return Indo(root)