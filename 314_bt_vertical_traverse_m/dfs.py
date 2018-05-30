# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = {}
        # x is depth, y is left/right
        def recur(root, x, y):
            if root:
                res.setdefault(y, []).append((x, root.val))
                recur(root.left, x + 1, y - 1)
                recur(root.right, x + 1, y + 1)
        
        recur(root, 0, 0)
        return [map(lambda x:x[1], sorted(res[k], key=lambda x:x[0])) for k in sorted(res.keys())]

# Recursion needs to be very careful
# Three properties, x, y and left/right

# Needs the help of x to sort vertically later. Otherwise the top/bottom is not guaranteed.
# Left will touch right, for example
# tree of 1, 2, 3, #, 4, #, #, #, 5, #, #, 5 first and 3 later.
# because we call recursion left to right

# Another issues is when sorting, we should only based on the key of x[0], this preserve the sequence of insertion. 
# Left/right property
# See line 23, key=lambda x:x[0]


# BFS definitely is easier to code and less mistakes