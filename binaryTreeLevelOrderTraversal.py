# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This is O(n^2) -- slow
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def height(root):
            if root is None:
                return 0
            lheight = height(root.left)
            rheight = height(root.right)

            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

        def givenLevel(root, level):
            if root is None:
                return
            if level == 1:
                l.append(root.val)
            else:
                givenLevel(root.left, level - 1)
                givenLevel(root.right, level - 1)

        res = []
        h = height(root)
        for i in range(1, h + 1):
            l = []
            givenLevel(root, i)
            res.append(l)
        return res

# Faster Solution
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        answer = []
        nodes = [root]

        while nodes:
            values = [node.val for node in nodes]
            answer.append(values)
            nodes = [child for node in nodes for child in (node.left, node.right) if child]

        return answer
