# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def recur(i, j):
            if i == j:
                return None
            max_i = i
            for k in range(i, j):
                if nums[k] > nums[max_i]:
                    max_i = k
            root = TreeNode(nums[max_i])
            root.left = recur(i, max_i)
            root.right = recur(max_i + 1, j)
            return root

        return recur(0, len(nums))

# No trick