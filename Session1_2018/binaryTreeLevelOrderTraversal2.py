# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        answer = []
        nodes = [root]

        while nodes:
            node_val = [node.val for node in nodes]
            answer.append(node_val)
            nodes = [child for node in nodes for child in (node.left, node.right) if child]

        return answer[::-1]
        
