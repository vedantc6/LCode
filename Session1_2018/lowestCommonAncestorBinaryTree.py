# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def LCA(node):
            if not node:
                return False
            left = LCA(node.left)
            right = LCA(node.right)

            mid = node == p or node == q

            if mid + left + right >= 2:
                self.result = node

            return mid or left or right

        LCA(root)
        return self.result
        
