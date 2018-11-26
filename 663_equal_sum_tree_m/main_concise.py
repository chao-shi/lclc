# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        sums = []
        def cal_sum(node):
            if node:
                sumv = node.val + cal_sum(node.left) + cal_sum(node.right)
                sums.append(sumv)
                return sumv
            else:
                return 0
        
        root_sum = cal_sum(root)
        if root_sum % 2 != 0:
            return False
        else:
            sums.pop()
            return root_sum / 2 in sums

# sums store the list of sums and the last sum will be root sum