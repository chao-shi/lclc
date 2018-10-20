# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        def recur(s, i):
            ii = i
            while i < len(s) and (s[i].isdigit() or s[i] == '-'):
                i += 1

            root = TreeNode(int(s[ii:i]))
            
            if i < len(s) and s[i] == '(':
                i += 1
                i, left = recur(s, i)
                i += 1
                root.left = left
                
            if i < len(s) and s[i] == '(':
                i += 1
                i, right = recur(s, i)
                i += 1
                root.right = right
            
            return i, root
        
        if not s:
            return None
        _, root = recur(s, 0)
        return root
    
# Negative numbers