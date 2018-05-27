# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxlen = 0
        def recur(root, start, end):
            if not root:
                return
            if end != None and end + 1 == root.val:
                end = root.val
            else:
                start, end = root.val, root.val
            self.maxlen = max(self.maxlen, end - start + 1)
            recur(root.left, start, end)
            recur(root.right, start, end)
        
        recur(root, None, None)
        return self.maxlen
    
# Good to store start, end instead of all sequence