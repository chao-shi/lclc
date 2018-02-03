# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return isMirror(root.left, root.right)
    
def isMirror(r1, r2):
    if r1 == r2 == None:
        return True
    elif r1 == None or r2 == None:
        return False
    return r1.val == r2.val and isMirror(r1.left, r2.right) and isMirror(r1.right, r2.left)