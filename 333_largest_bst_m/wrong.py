# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_v = 0
        def recur(root, lower, upper):
            if root == None:
                return 0
            if lower < root.val < upper:
                left_size = recur(root.left, lower, root.val)
                right_size = recur(root.right, root.val, upper)
                if left_size != None and right_size != None:
                    tree_size = 1 + left_size + right_size
                    self.max_v = max(self.max_v, tree_size)
                    return tree_size
                else:
                    return None
            else:
                # Wrong here, even this case we need to explore
                return None
        recur(root, -sys.maxint, sys.maxint)
        return self.max_v