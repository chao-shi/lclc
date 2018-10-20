# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.last = None
        self.min_abs_diff = sys.maxint

        def in_order(root):
            if root:
                in_order(root.left)
                if self.last != None:
                    abs_diff = root.val - self.last.val
                    self.min_abs_diff = min(self.min_abs_diff, abs_diff)
                self.last = root
                in_order(root.right)
        
        in_order(root)
        return self.min_abs_diff
                