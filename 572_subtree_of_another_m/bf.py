# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def check_same(s, t):
            if s == t == None:
                return True
            elif s == None or t == None:
                return False
            else:
                return s.val == t.val and check_same(s.left, t.left) and check_same(s.right, t.right)
        
        def recur(root, t):
            res = check_same(root, t)
            if root:
                res = res or recur(root.left, t) or recur(root.right, t)
            return res
        
        return recur(s, t)

# O(mn)