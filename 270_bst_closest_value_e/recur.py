# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closer(self, v1, v2, target):
        if v1 == None:
            return v2
        elif v2 == None:
            return v1
        return v1 if abs(v1 - target) < abs(v2 - target) else v2

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        elif root.val == target:
            return root.val
        elif root.val < target:
            return self.closer(root.val, self.closestValue(root.right, target), target)
        else:
            return self.closer(root.val, self.closestValue(root.left, target), target)