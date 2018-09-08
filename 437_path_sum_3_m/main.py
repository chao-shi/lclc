# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.cnt = 0
        
        def recur(root, accu_sums, last_sum):
            if not root:
                return
            last_sum += root.val

            self.cnt += accu_sums.get(last_sum - sum, 0)
            accu_sums[last_sum] = accu_sums.get(last_sum, 0) + 1
            
            recur(root.left, accu_sums, last_sum)
            recur(root.right, accu_sums, last_sum)
            accu_sums[last_sum] -= 1
        
        recur(root, {0:1}, 0)
        return self.cnt  