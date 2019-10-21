# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def util(node):
            if node:
                util(node.left)
                ans.append(node.val)
                util(node.right)

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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        ans = []
        stack = []
        while True:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                else:
                    root = stack.pop()
                    ans.append(root.val)
                    root = root.right
        return ans
