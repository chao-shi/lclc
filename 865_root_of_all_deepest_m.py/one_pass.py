# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.maxdepth = 0
        self.cand = None

        def recur(root, depth):
            if not root:
                return 0
            d1, d2 = recur(root.left, depth+1), recur(root.right, depth+1)
            if d1 == d2 and d1 + depth + 1 >= self.maxdepth:
                self.cand = root
                self.maxdepth = max(self.maxdepth, d1 + depth + 1)
            return 1 + max(d1, d2)
        recur(root, 0)
        return self.cand