# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        dh = TreeNode(None)
        self.tail = dh
        
        def recur(root):
            if root:
                self.tail.right, self.tail = root, root
                left, right = root.left, root.right
                root.left, root.right = None, None
                recur(left)
                recur(right)
        
        recur(root)

# Approach 3: append node one by one
# Best approach
# Pre-order one by one
# Important line 21 detach subtree first.
# recursion on left tree will pollute root.right