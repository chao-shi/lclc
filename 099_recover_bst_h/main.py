# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root:
                return
            for n in inorder(root.left):
                yield n
            yield root
            for n in inorder(root.right):
                yield n

        last = None
        swap1, swap2 = None, None
        for node in inorder(root):
            if last and last.val > node.val:
                swap2 = node
                if not swap1:
                    swap1 = last
            last = node
        
        swap1.val, swap2.val = swap2.val, swap1.val

# Good solution using generator
# Good using last, optimizaed for logic lobkc 26