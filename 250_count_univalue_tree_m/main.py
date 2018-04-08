# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        # Return None if not uni-value
        # Otherwise return the value
        # Empty tree is a little tricky
        def countTree(root):
            if not root:
                return None

            lv = countTree(root.left)
            rv = countTree(root.right)
            if (not root.left or lv == root.val) and (not root.right or rv == root.val):
                self.count += 1
                return root.val
            return None
        
        countTree(root)
        return self.count