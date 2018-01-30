# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # return value different from dp value        
        if n == 0:
            return []

        def makeTree(val, left, right):
            root = TreeNode(val)
            root.left, root.right = left, right
            return root

        # 1 .. n tree represent by [0, n]
        m = [[[] for i in range(n+1)] for j in range(n+1)]
        for i in range(n+1):
            m[i][i].append(None)
        for length in range(1, n+1):
            for j in range(length, n+1):
                i = j - length
                # BST for range of elements of [i+1, j]
                # left tree will be [i+1, k-1] which maps to [i][k-1]
                # right tree will be [k+1, j] which maps to [k][j]
                m[i][j] = [makeTree(k, left, right) for k in range(i + 1, j + 1) for left in m[i][k-1] for right in m[k][j]]
        return m[0][n]

# Careful about range in line 21, line 29
# How to write it clean ???