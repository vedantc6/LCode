# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def helper(node):
            if not node: return 0
            left_len = helper(node.left)
            right_len = helper(node.right)
            l_pointer = r_pointer = 0
            if node.left and node.left.val == node.val:
                l_pointer = left_len + 1
            if node.right and node.right.val == node.val:
                r_pointer = right_len + 1
            self.res = max(self.res, l_pointer + r_pointer)
            return max(l_pointer, r_pointer)

        helper(root)
        return self.res

        
