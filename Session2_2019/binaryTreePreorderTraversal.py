# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def util(node):
            if node:
                ans.append(node.val)
                util(node.left)
                util(node.right)

        if not root:
            return None
        ans = []
        util(root)
        return ans

# Iterative
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        ans = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                ans.append(root.val)
                stack.append(root.right)
                stack.append(root.left)

        return ans
