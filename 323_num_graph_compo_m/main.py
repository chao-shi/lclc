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
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(range(n))
        for e in edges:
            uf.union(e[0], e[1])
        return uf.set_cnt