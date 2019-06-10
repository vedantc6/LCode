# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, cur_sum, lnodes, result):
        if not root.left and not root.right and cur_sum == root.val:
            lnodes.append(root.val)
            result.append(lnodes)
        if root.left:
            self.dfs(root.left, cur_sum - root.val, lnodes + [root.val], result)
        if root.right:
            self.dfs(root.right, cur_sum - root.val, lnodes + [root.val], result)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        self.dfs(root, sum, [], result)
        return result

# Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = [(root, sum, [])]
        while stack:
            node, cur_sum, lnodes = stack.pop()
            if not node.left and not node.right and node.val == cur_sum:
                res.append(lnodes + [node.val])
            if node.left:
                stack.append((node.left, cur_sum - node.val, lnodes + [node.val]))
            if node.right:
                stack.append((node.right, cur_sum - node.val, lnodes + [node.val]))
        return res
