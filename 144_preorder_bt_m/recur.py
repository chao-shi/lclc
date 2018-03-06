# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        def recur(root):
            if not root:
                return
            l.append(root.val)
            recur(root.left)
            recur(root.right)
        recur(root)
        return l