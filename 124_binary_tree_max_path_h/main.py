# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = None
        # return longest from root, not necessary root-leaf
        def recur(root):
            # different from other root-leaf path
            # Ok to return 0
            if root == None:
                return 0
            left_longest = recur(root.left)
            right_longest = recur(root.right)
            self.max = max(self.max, root.val + left_longest + right_longest)
            # Ok for the case when left or right is empty
            return max(max(left_longest, right_longest) + root.val, 0)
        
        recur(root)
        return self.max

# Line 25 !!!, max(0)