# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapp = {}
        for i in range(len(inorder)):
            mapp[inorder[i]] = i
        def buildOriginalTree(postorder, posStart, posEnd, inorder, inStart, inEnd, mapp):
            if posStart > posEnd or inStart > inEnd:
                return None
            root = TreeNode(postorder[posEnd])
            inRoot = mapp[root.val]
            inNumL = inRoot - inStart
            root.left = buildOriginalTree(postorder, posStart, posStart + inNumL - 1, inorder, inStart, inRoot - 1, mapp)
            root.right = buildOriginalTree(postorder, posStart + inNumL, posEnd - 1, inorder, inRoot + 1, inEnd, mapp)

            return root
        return buildOriginalTree(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1, mapp)