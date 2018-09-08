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
        return self.recur(sum, root, {0:1}, 0)
        
    def recur(self, sum, root, accu_sums, last_sum):
        if not root:
            return 0
        last_sum += root.val

        cnt = accu_sums.get(last_sum - sum, 0)
        accu_sums[last_sum] = accu_sums.get(last_sum, 0) + 1

        cnt += self.recur(sum, root.left, accu_sums, last_sum)
        cnt += self.recur(sum, root.right, accu_sums, last_sum)
        accu_sums[last_sum] -= 1
        
        return cnt