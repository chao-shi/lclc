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
        def reverse_in_order(root, accu_right_sum):
            if root:
                right_sum = reverse_in_order(root.right, accu_right_sum)
                root_val = root.val
                root.val += right_sum + accu_right_sum
                left_sum = reverse_in_order(root.left, root.val)
                return root_val + right_sum + left_sum
            else:
                return 0
        
        reverse_in_order(root, 0)
        return root