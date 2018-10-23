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
        
        self.ans = 0

        def recur(root):
            if not root:
                return 0, 0

            ld, li, rd, ri = 1, 1, 1, 1
            
            sub_d, sub_i = recur(root.left)
            if root.left and root.left.val == root.val - 1:
                ld = sub_d + 1
            elif root.left and root.left.val == root.val + 1:
                li = sub_i + 1
        
            sub_d, sub_i = recur(root.right)
            if root.right and root.right.val == root.val - 1:
                rd = sub_d + 1
            elif root.right and root.right.val == root.val + 1:
                ri = sub_i + 1
            
            self.ans = max(self.ans, max(ld + ri, li + rd) - 1) 

            maxd, maxi = max(ld, rd), max(li, ri)
            return (maxd, maxi)
        
        recur(root)
        return self.ans
        