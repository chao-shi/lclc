# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0
        def recur(root):
            if not root:
                return 0
            else:
                l_len = recur(root.left)
                r_len = recur(root.right)
                max_root_len = 1
                path_len = 1
                if l_len and root.left.val == root.val:
                    path_len += l_len
                    max_root_len = max(max_root_len, 1 + l_len)
                if r_len and root.right.val == root.val:
                    path_len += r_len
                    max_root_len = max(max_root_len, 1 + r_len)
                self.max_len = max(self.max_len, path_len)
                return max_root_len
        
        recur(root)
        return max(0, self.max_len - 1) 