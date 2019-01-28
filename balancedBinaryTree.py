# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        if not root:
            return True

        left = height(root.left)
        right = height(root.right)

        if abs(left - right) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
