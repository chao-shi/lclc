# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recur(root):
            if not root:
                return []
            elif root.left == root.right == None:
                return [root.val]
            else:
                l2, r2 = recur(root.left), recur(root.right)
                vals = sorted(set(l2 + r2))
                return vals[:2]
        
        top2 = recur(root)
        return top2[1] if len(top2) == 2 else -1