# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.cur = None
        def recur(root):
            if not root:
                return
            recur(root.right)
            recur(root.left)
            # root.left and root.right concatecated. root.left and root.right still attached
            root.left, root.right = None, self.cur
            self.cur = root
        recur(root)

# Brilliant idea, append the list in the reverse order.
# This solves the issue of polluting root.right