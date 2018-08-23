# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recur(root):
            if root == None:
                return 0
            sum = recur(root.right)
            if root.left != None and root.left.left == root.left.right == None:
                sum += root.left.val
            else:
                sum += recur(root.left)
            return sum
        return recur(root)