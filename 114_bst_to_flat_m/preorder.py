# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.cur = None
        def recur(root):
            if not root:
                return
            self.cur = root
            recur(root.left)
            prev = self.cur
            recur(root.right)
            prev.right = root.right
            if root.left:
                root.right = root.left
            root.left = None
        recur(root)
        
# Approach two, preorder traversal tree merge
# self.cur follows preorder sequence. 
# line 20 prev is assigned to be right most node of left tree (or root itself if root is empty)
