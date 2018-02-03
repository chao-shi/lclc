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
        def concat(head1, tail1, head2, tail2):
            dh = TreeNode(None)
            tail = dh
            tail.right = head1
            if head1:
                tail = tail1
            tail.right = head2
            if head2:
                tail = tail2
            return dh.right, tail
        
        def recur(root):
            if not root:
                return None, None
            lh, lt = recur(root.left)
            rh, rt = recur(root.right)
            root.left = None
            head, tail = root, root
            head, tail = concat(head, tail, lh, lt)
            head, tail = concat(head, tail, rh, rt)
            return head, tail
        
        recur(root)
        
# Careful Careful, clear left child on line 30