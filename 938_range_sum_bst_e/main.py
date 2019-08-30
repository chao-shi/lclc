# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.sumv = 0

        def recur(root):
            if not root:
                return
            if L <= root.val <= R:
                self.sumv += root.val     
            
            if not root.val < L:
                recur(root.left)
            if not root.val > R:
                recur(root.right)
        
        recur(root)
        return self.sumv