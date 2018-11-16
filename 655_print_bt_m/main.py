# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        m = depth(root)
        n = 2 ** m - 1
        matrix = [[""] * n for _ in range(m)]

        def recur(root, x, y):
            if not root:
                return
            print x, y
            matrix[x][y] = str(root.val)

            branch_step = 2 ** (m - x - 2)
            recur(root.left, x + 1, y - branch_step)
            recur(root.right, x + 1, y + branch_step)

        
        recur(root, 0, n / 2)
        return matrix
        

# The trick of presetting all the slots