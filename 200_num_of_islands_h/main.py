class UnionFind(object):
    def __init__(self, values):
        self.parent = {v : v for v in values}
        self.size = {v:1 for v in values}
        self.set_cnt = len(values)
    
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
            self.set_cnt -= 1
        else:
            self.parent[ru] = rv
            self.size[rv] += self.size[ru]
            self.set_cnt -= 1

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind([(i, j) for i in range(m) for j in range(n) if grid[i][j] == "1"])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if i + 1 < m and grid[i+1][j] == "1":
                        uf.union((i, j), (i+1, j))
                    if j + 1 < n and grid[i][j+1] == "1":
                        uf.union((i, j), (i, j+1))
        
        return uf.set_cnt

# Careful in block 41, still needs to iterate range(m), range(n)
# I thought about only iteration on grid[:-1][:-1], this is wrong
# Forget the horizontal connection on last row.