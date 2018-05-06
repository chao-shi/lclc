# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        left_parent, right_parent = sys.maxint, -sys.maxint
        p = root
        while p and p.val != target:
            if p.val < target:
                right_parent = p.val
                p = p.right
            else:
                left_parent = p.val
                p = p.left
        if p:
            return p.val
        return left_parent if abs(left_parent - target) < abs(right_parent - target) else right_parent

# Brilliant usage of sys.maxint