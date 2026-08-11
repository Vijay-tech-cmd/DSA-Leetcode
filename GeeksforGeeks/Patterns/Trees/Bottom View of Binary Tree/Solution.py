'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
        queue = deque([(root, 0)])
        ans = {}
        level = 0
        while queue:
            node, level = queue.popleft()
            ans[level] = node.data
            if node.left:
                queue.append((node.left, level-1))
            if node.right:
                queue.append((node.right, level+1))
        res = []
        for i in sorted(ans):
            res.append((ans[i]))
        return res