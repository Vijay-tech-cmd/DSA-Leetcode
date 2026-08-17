# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        mpp = {}
        target = None
        def bfsToMapParents(root):
            queue = deque([root])
            nonlocal target
            while queue:
                node = queue.popleft()
                if node.val == start:
                    target = node
                if node.left:
                    mpp[node.left] = node
                    queue.append(node.left)
                if node.right:
                    mpp[node.right] = node
                    queue.append(node.right)
        bfsToMapParents(root)
        queue = deque([target])
        visit = {target}
        maxii = 0
        while queue:
            level_size = len(queue)
            flag = 0
            for _ in range(level_size):
                node = queue.popleft()
                if node.left and node.left not in visit:
                    visit.add(node.left)
                    queue.append(node.left)
                    flag = 1
                if node.right and node.right not in visit:
                    visit.add(node.right)
                    queue.append(node.right)
                    flag = 1
                if node in mpp:
                    parent = mpp[node]
                    if parent not in visit:
                        visit.add(parent)
                        queue.append(parent)
                        flag = 1
            if flag:
                maxii += 1
        return maxii