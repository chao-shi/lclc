# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def recur(root):
            if not root:
                return ""
            elif not root.left and not root.right:
                return "{}".format(root.val)
            elif not root.right:
                return "{}({})".format(root.val, recur(root.left))
            else:
                return "{}({})({})".format(root.val, recur(root.left), recur(root.right))
        
        # None returns ""
        return recur(t)