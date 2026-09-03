# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Identify(root, minVal, maxVal):
            if not root:
                return True
            if root.val <= minVal or root.val >= maxVal:
                return False
            return Identify(root.left, minVal, root.val) and Identify(root.right, root.val, maxVal)
        return Identify(root, float('-inf'), float('inf'))