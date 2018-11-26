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
        sum_map = collections.defaultdict(set)
        def cal_sum(node):
            if node:
                sumv = node.val + cal_sum(node.left) + cal_sum(node.right)
                sum_map[sumv].add(node)
                return sumv
            else:
                return 0
        
        root_sum = cal_sum(root)
        if root_sum % 2 != 0:
            return False
        else:
            if root in sum_map[root_sum / 2]:
                sum_map[root_sum / 2].remove(root)
            return len(sum_map[root_sum/2]) > 0

# Corner case of   0
#               -1,  1