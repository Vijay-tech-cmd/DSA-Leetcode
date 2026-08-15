# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def markParent(root, parent_track, target):
            queue = deque([root])
            while queue:
                current = queue.popleft()
                if current.left:
                    parent_track[current.left] = current
                    queue.append(current.left)
                if current.right:
                    parent_track[current.right] = current
                    queue.append(current.right)
        parent_track = {}
        markParent(root, parent_track, target)
        visited = {target}
        queue = deque([target])
        current_level = 0
        while queue and current_level < k:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.popleft()
                if current.left and current.left not in visited:
                    queue.append(current.left)
                    visited.add(current.left)
                if current.right and current.right not in visited:
                    queue.append(current.right)
                    visited.add(current.right)
                if current in parent_track:
                    parent = parent_track[current]
                    if parent not in visited:
                        visited.add(parent)
                        queue.append(parent)
            current_level += 1
        res = []
        while queue:
            res.append(queue.popleft().val)
        return res