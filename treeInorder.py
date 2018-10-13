# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def wrapper(root):
            if root:
                wrapper(root.left)
                l.append(root.val)
                wrapper(root.right)

        l = []
        wrapper(root)
        return l
        
