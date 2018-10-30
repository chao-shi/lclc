# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        def recur(root, depth):
            if not root:
                return
            elif depth == d - 1:
                new_left = TreeNode(v)
                new_right = TreeNode(v)
                new_left.left = root.left
                new_right.right = root.right
                root.left, root.right = new_left, new_right
            else:
                recur(root.left, depth + 1)
                recur(root.right, depth + 1)
                
        
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        else:
            recur(root, 1)
            return root