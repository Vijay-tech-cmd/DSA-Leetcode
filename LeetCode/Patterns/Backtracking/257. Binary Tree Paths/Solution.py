# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def RootToNode(node, path):
            if not node:
                return
            path.append(str(node.val))
            if node.left is None and node.right is None:
                ans.append("->".join(path))
                path.pop()
                return
            RootToNode(node.left, path)
            RootToNode(node.right, path)

            path.pop()
        RootToNode(root, [])
        return ans
            