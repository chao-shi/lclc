# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recur(root):
            if root == None:
                return 0
            lh, rh = recur(root.left), recur(root.right)
            if lh == 0:
                return 1 + rh
            elif rh == 0:
                return 1 + lh
            else:
                return 1 + min(lh, rh)
        return recur(root)
    
# A clean way