class UnionFind(object):
    def __init__(self, values):
        self.parent = {v : v for v in values}
        self.size = {v:1 for v in values}
        self.set_cnt = len(values)
    
    def add(self, u):
        self.parent[u] = u
        self.size[u] = 1
        self.set_cnt += 1
    
    def has(self, u):
        return u in self.parent

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
        self.set_cnt -= 1
        

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind([])
        res = []
        for p in positions:
            uf.add(tuple(p))
            for v in [(0,1), (1,0), (0, -1), (-1,0)]:
                x, y = p[0] + v[0], p[1] + v[1]
                if uf.has((x, y)):
                    uf.union(tuple(p), (x, y))
            res.append(uf.set_cnt)
        return res
        
        
# Technically m and n not not needed
# Complexity is O(len(pos))
# The UF tree never grows more than len(pos), and the height starts with 1. Like a heapify algorithm
# That's why it is not O(len(pos) * log(len(pos)))