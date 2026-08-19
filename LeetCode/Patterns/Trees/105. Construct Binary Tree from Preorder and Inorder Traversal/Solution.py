# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapp = {}
        for i in range(len(inorder)):
            mapp[inorder[i]] = i
        def buildSecondTree(preorder, preStart, preEnd, inorder, inStart, inEnd, mapp):
            if preStart > preEnd or inStart > inEnd:
                return None
            root = TreeNode(preorder[preStart])
            inRoot = mapp[root.val]
            inNumLeft = inRoot - inStart
            
            root.left = buildSecondTree(preorder, preStart + 1, preStart + inNumLeft, inorder, inStart, inRoot - 1, mapp)
            root.right = buildSecondTree(preorder, preStart + inNumLeft + 1, preEnd, inorder, inRoot + 1, inEnd, mapp)
            return root
        return buildSecondTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, mapp)