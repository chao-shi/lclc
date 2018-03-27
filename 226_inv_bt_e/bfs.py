# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = [root]
        while q:
            top = q.pop()
            if top:
                top.left, top.right = top.right, top.left
                q.extend([top.left, top.right])
        return root