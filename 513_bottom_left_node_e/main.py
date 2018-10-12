# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = -1
        self.ans = None
        
        def recur(root, depth):
            if not root:
                return
            elif root.left == root.right == None and depth > self.max_depth:
                self.ans = root
                self.max_depth = depth
            else:
                recur(root.left, depth + 1)
                recur(root.right, depth + 1)
        
        recur(root, 0)
        return self.ans.val
        