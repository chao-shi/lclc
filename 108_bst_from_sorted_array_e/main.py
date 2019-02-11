# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def recur(start, end):
            if start == end:
                return None
            mid = (start + end) / 2
            root = TreeNode(nums[mid])
            root.left = recur(start, mid)
            root.right = recur(mid + 1, end)
            return root
        return recur(0, len(nums))