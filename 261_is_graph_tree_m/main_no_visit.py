class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,
        def visit(v):
            map(visit, neighbors.pop(v, []))
        visit(0)
        return len(edges) == n-1 and not neighbors

# This approach builds neighbor map and then pop from the same map. 

# Key point is that we need to populate every node in line 8 (Very important)
# popping from the neighbors map means it was visited.

# Checkout here
# https://leetcode.com/problems/graph-valid-tree/discuss/69020/8-10-lines-Union-Find-DFS-and-BFS