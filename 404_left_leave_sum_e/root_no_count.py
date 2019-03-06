# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recur(root, isLeftChild):
            if not root:
                return 0
            elif root.left == None and root.right == None and isLeftChild:
                return root.val
            else:
                return recur(root.left, True) + recur(root.right, False)
        
        return recur(root, False)
    
# One-node tree count as left leave