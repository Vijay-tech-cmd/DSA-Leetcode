# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        stack_container = []
        stack_container.append(root)
        while stack_container:
            curr = stack_container.pop()
            if curr.right:
                stack_container.append(curr.right)
            if curr.left:
                stack_container.append(curr.left)
            if stack_container:
                curr.right = stack_container[-1]
            curr.left = None