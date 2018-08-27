class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        bit_map = [[0] * n for i in range(m)]

        def trace_source(i, j, mask):
            if bit_map[i][j] & mask == 0:
                bit_map[i][j] |= mask
                for v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ii, jj = i + v[0], j + v[1]
                    if 0 <= ii < m and 0 <= jj < n and matrix[ii][jj] >= matrix[i][j]:
                        trace_source(ii, jj, mask)
        
        for i in range(m):
            trace_source(i, 0, 1)
            trace_source(i, n - 1, 2)
        
        for j in range(n):
            trace_source(0, j, 1)
            trace_source(m - 1, j, 2)
        
        res = [[i, j] for i in range(m) for j in range(n) if bit_map[i][j] == 3]
        return res
            
            
        
# Union find does not work here. because the transitive is violated.
# A -> B and A -> C, but B anc C can belong to different water system.