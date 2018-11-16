# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def size(root):
            if root:
                return 1 + size(root.left) + size(root.right)
            else:
                return 0

        def in_order(root):
            if root:
                for n in in_order(root.left):
                    yield n
                yield root.val
                for n in in_order(root.right):
                    yield n
                    
        def in_order_rev(root):
            if root:
                for n in in_order_rev(root.right):
                    yield n
                yield root.val
                for n in in_order_rev(root.left):
                    yield n
        
        n = size(root)
        iter1, iter2 = in_order(root), in_order_rev(root)
        
        h1, h2 = None, None
        for _ in range(n - 1):
            if h1 == None:
                h1 = iter1.next()
            if h2 == None:
                h2 = iter2.next()
                
            if h1 + h2 == k:
                return True
            elif h1 + h2 < k:
                h1 = None
            else:
                h2 = None
        return False