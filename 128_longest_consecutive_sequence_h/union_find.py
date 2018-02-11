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
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uf = UnionFind(nums)
        nums = set(nums)
        for num in nums:
            if num + 1 in nums:
                uf.union(num, num + 1)
            # if num - 1 in nums:
            #     uf.union(num, num - 1)

        if len(nums) == 0:
            return 0
        return max(uf.size.values())

# Line 17 important
# Union find with weighted parent and path compression

# Union find start with fixed elements

# Not the best approach. Why
# This union find is better for case where union happen more "UNPREDICTABLY"

# Line 38 not needed. Only one directional union