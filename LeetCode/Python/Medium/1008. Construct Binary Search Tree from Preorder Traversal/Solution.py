# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        index = 0
        def build(upperBoundary):
            nonlocal index
            if index == len(preorder) or preorder[index] > upperBoundary:
                return None
            root = TreeNode(preorder[index])
            index += 1
            root.left = build(root.val)
            root.right = build(upperBoundary)
            return root
        return build(float('inf'))