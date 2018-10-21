# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path = 0
        # This problem OK to terminate on Null. 
        # Some root leaf path problem is not OK
        # Here for one sided subtree, we may not check the "real" root-leaf path
        # But this "fake" path is inferior to the real one
        def recur(root):
            if not root:
                return 0
            left_path = recur(root.left)
            right_path = recur(root.right)
            self.max_path = max(self.max_path, left_path + 1+ right_path)
            return 1 + max(left_path, right_path)
        
        if not root:
            return 0

        recur(root)
        return self.max_path - 1