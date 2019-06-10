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
        parent = root.val
        p_val = p.val
        q_val = q.val

        if p_val > parent and q_val > parent:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent and q_val < parent:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
