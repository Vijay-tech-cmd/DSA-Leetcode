# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pushLeft(self, node):
        while node:
            self.left.append(node)
            node = node.left
    def pushRight(self, node):
        while node:
            self.right.append(node)
            node = node.right
    def nextSmall(self):
        node = self.left.pop()
        if node.right:
            self.pushLeft(node.right)
        return node.val
    def nextLarge(self):
        node = self.right.pop()
        if node.left:
            self.pushRight(node.left)
        return node.val
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.left = []
        self.right = []
        self.pushLeft(root)
        self.pushRight(root)

        i = self.nextSmall()
        j = self.nextLarge()
        while i < j:
            summing = i + j
            if summing == k:
                return True
            elif summing < k:
                i = self.nextSmall()
            else:
                j = self.nextLarge()
        return False