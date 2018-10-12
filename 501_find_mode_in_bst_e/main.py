# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def count(root):
            if not root:
                return {}
            left_cnt = count(root.left)
            right_cnt = count(root.right)
            for k in right_cnt:
                left_cnt[k] = left_cnt.get(k, 0) + right_cnt[k]
            left_cnt[root.val] = left_cnt.get(root.val, 0) + 1
            return left_cnt
        
        if not root:
            return []
        cnt = count(root)
        max_f = max(cnt.values())
        return [k for k in cnt if cnt[k] == max_f]
        