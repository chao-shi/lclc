# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recur(root):
            if not root:
                return 0, 0
            l_max, l_not_root_max = recur(root.left)
            r_max, r_not_root_max = recur(root.right)
            
            v1 = l_max + r_max
            v2 = root.val + l_not_root_max + r_not_root_max
            
            return max(v1, v2), v1
        
        m, _ = recur(root)
        return m