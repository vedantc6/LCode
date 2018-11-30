# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res, level = [], [root]
        direction = 1
        while level:
            res.append([node.val for node in level][::direction])
            direction *= -1
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res
            
