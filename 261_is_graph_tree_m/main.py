class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        emap = {}
        for u, v in edges:
            emap.setdefault(u, []).append(v)
            emap.setdefault(v, []).append(u)

        visited = set()
        def recur(n):
            if n not in visited:
                visited.add(n)
                map(recur, emap.get(n, []))
        recur(0)
        return len(visited) == n

# The major ideas here is to 
# Number of edges is n-1 and connected (Easier and implemented here)
# Number of edges is n-1 and cycle detection