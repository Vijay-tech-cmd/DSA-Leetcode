# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev = TreeNode(float('-inf'))
        first = None
        middle = None
        last = None
        def inorder(node):
            nonlocal prev, first, middle, last
            if not node:
                return 
            inorder(node.left)
            if node.val < prev.val:
                if first == None:
                    first = prev
                    middle = node
                else:
                    last = node
            prev = node
            inorder(node.right)
        inorder(root)
        if first and last:
            first.val, last.val = last.val, first.val
        elif first and middle:
            first.val, middle.val = middle.val, first.val