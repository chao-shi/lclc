# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def recur(root, val):
            if not root:
                return None
            elif root.val == val:
                return root
            elif root.val < val:
                return recur(root.right, val)
            else:
                return recur(root.left, val)
            
        return recur(root, val)
        