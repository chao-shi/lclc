# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recur(root, minv, maxv):
            if not root:
                return True
            elif root.val <= minv or root.val >= maxv:
                return False
            else:
                return recur(root.left, minv, root.val) and recur(root.right, root.val, maxv)
        return recur(root, -sys.maxint, sys.maxint)
        