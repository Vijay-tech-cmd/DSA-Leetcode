# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, path):
            if not node:
                return 
            path.append(node.val)
            if node.left is None and node.right is None:
                ans.append("->".join(map(str, path[:])))
            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()
        dfs(root, [])
        return ans