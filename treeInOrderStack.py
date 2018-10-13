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
        stack = []
        l = []
        current = root
        finished = 0
        while not finished:
            if current != None:
                stack.append(current)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    l.append(current.val)
                    current = current.right
                else:
                    finished = 1

        return l
            
