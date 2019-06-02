# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def recur(root, val):
            if not root:
                return TreeNode(val)
            elif root.right == None and val > root.val:
                root.right = TreeNode(val)
            elif root.left == None and val < root.val:
                root.left = TreeNode(val)
            elif val < root.val:
                recur(root.left, val)
            else:
                recur(root.right, val)
            return root
        return recur(root, val)