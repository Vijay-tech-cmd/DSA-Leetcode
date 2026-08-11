# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def Right(node, level):
            if not node:
                return
            if level == len(ans):
                ans.append(node.val)
            Right(node.right, level + 1)
            Right(node.left, level + 1)
        Right(root, 0)
        return ans