# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def construct_paths(self, root, path):
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                self.paths.append(path)
            else:
                path += '->'
                self.construct_paths(root.left, path)
                self.construct_paths(root.right, path)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.paths = []
        self.construct_paths(root, '')
        return self.paths

# Stacks implementation
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths
