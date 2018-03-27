# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def in_order(root):
            if root:
                for n in in_order(root.left):
                    yield n
                yield root
                for n in in_order(root.right):
                    yield n
        
        cnt = 1
        for node in in_order(root):
            if cnt == k:
                return node.val
            cnt += 1

# BST inorder generator
# Cleaner than writing inorder function and set global variables