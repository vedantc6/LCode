# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBSTUtil(self, node, minlim, maxlim):
        if not node:
            return True
        if node.val < minlim or node.val > maxlim:
            return False
        return self.isValidBSTUtil(node.left, minlim, node.val-1) and self.isValidBSTUtil(node.right, node.val+1, maxlim)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        minval, maxval = -2147483648, 2147483647
        return self.isValidBSTUtil(root, minval, maxval)

        
