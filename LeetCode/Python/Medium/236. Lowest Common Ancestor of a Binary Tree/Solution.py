# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def Lowest(node, p, q):
            if not node:
                return None
            if node is p or node is q:
                return node
            left = Lowest(node.left, p, q)
            right = Lowest(node.right, p, q)

            if left is not None and right is not None:
                return node
            elif left is not None:
                return left
            else:
                return right
        return Lowest(root, p, q)
        