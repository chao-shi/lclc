# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recur(root):
            if not root:
                return True, 0, 0
            else:
                r1, mind1, maxd1 = recur(root.left)
                if not r1:
                    return False, -1, -1
                r2, mind2, maxd2 = recur(root.right)
                if not r2:
                    return False, -1, -1
                
                valid = 1 >= maxd1 - mind2 >= 0 and mind1 >= maxd2
                return valid, mind2 + 1, maxd1 + 1
            
        res, _, _ = recur(root)
        return res