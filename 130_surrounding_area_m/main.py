class UnionFind(object):
    def __init__(self, values):
        self.parent = {v : v for v in values}
        self.size = {v:1 for v in values}
    
    def root(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
        
    def find(self, u, v):
        return self.root(u) == self.root(v)
    
    def union(self, u, v):
        ru, rv = self.root(u), self.root(v)
        # Important, don't want to double the tree size
        if ru == rv:
            return 
        if self.size[ru] > self.size[rv]:
            self.parent[rv] = ru
            self.size[ru] += self.size[rv]
        else:
            self.parent[ru] = rv
            self.size[rv] += self.size[ru]

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        n, m = len(board), len(board[0])

        def out(i, j):
            return i < 0 or j < 0 or i >= n or j >= m

        def border(i, j):
            return i == 0 or j == 0 or i == n - 1 or j == m - 1

        # indexes = [(i, j) for i in range(-1, n + 1, 1) for j in range(-1, m + 1, 1) if out(i, j) or board[i][j] == 'O']
        # Better keep only one "OCEAN" element rather than all boundaries
        # This saves the work of union all the ocean elements
        indexes = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 'O'] + [(-1, -1)]
        uf = UnionFind(indexes)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    # four direction
                    for v in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                        vi, vj = v[0] + i, v[1] + j
                        if not out(vi, vj) and board[vi][vj] == 'O':
                            uf.union((i, j), (vi, vj))
                        elif out(vi, vj):
                            uf.union((i, j), (-1, -1))
                    
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not uf.find((i, j), (-1, -1)):
                    board[i][j] = 'X'