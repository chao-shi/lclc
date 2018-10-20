# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.accu_sum = 0
        def reverse_in_order(root):
            if root:
                reverse_in_order(root.right)
                self.accu_sum += root.val
                root.val = self.accu_sum
                reverse_in_order(root.left)
        
        reverse_in_order(root)
        return root