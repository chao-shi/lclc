"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def recur(i, j, n):
            if n == 1:
                return Node(grid[i][j] == 1, True, None, None, None, None)

            tl, tr, bl, br = recur(i, j, n/2), recur(i, j+n/2, n/2), recur(i+n/2, j, n/2), recur(i+n/2, j+n/2, n/2)
            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
                return Node(tl.val, True, None, None, None, None)
            else:
                return Node(None, False, tl, tr, bl, br)
        
        return recur(0, 0, len(grid))
