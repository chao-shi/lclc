# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        def recur(root, base):
            if root == None:
                return
            elif root.left == None and root.right == None:
                self.total += base * 10 + root.val
            else:
                base = base * 10 + root.val
                recur(root.left, base)
                recur(root.right, base)
        
        recur(root, 0)
        return self.total