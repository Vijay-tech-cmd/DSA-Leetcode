# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        x = 0
        y = 0
        queue = deque([(root, 0, 0)])
        columns = defaultdict(list)
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node, x, y = queue.popleft()
                columns[x].append((y, node.val))
                if node.left:
                    queue.append((node.left, x-1, y+1))
                if node.right:
                    queue.append((node.right, x+1, y+1))
        result = []
        for x in sorted(columns.keys()):
            columns[x].sort()
            result.append([value for y, value in columns[x]])
        return result