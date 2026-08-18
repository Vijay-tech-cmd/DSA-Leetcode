# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def leftHeight(node):
            heightL = 0
            while node:
                node = node.left
                heightL += 1
            return heightL
        def rightHeight(node):
            heightR = 0
            while node:
                node = node.right
                heightR += 1
            return heightR
        if not root:
            return 0
        lh = leftHeight(root)
        rh = rightHeight(root)
        if lh == rh:
            return (2 ** lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)