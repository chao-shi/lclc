# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        
        def recur(root):
            if not root:
                return 0
            lsum, rsum = recur(root.left), recur(root.right)
            self.total += abs(lsum - rsum)
            return root.val + lsum + rsum
        
        recur(root)
        return self.total
        