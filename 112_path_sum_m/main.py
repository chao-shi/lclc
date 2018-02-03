# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def recur(root, sum):
            if root == None:
                return False
            elif root.left == None and root.right == None:
                return root.val == sum
            else:
                return recur(root.left, sum - root.val) or recur(root.right, sum - root.val)
        return recur(root, sum)
    
# The corner case is None, 0
# Careful of example of [1, 2] where 1 is root and 2 is right child. and target is 1

# block 16 is very very important