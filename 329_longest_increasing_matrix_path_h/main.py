class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        mt = {}
        def recur(i, j):
            if (i, j) in mt:
                return mt[(i, j)]
            
            maxv = 1
            for v in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ii, jj = i + v[0], j + v[1]
                if 0 <= ii < m and 0 <= jj < n and matrix[i][j] < matrix[ii][jj]:
                    maxv = max(maxv, 1 + recur(ii, jj))
            
            mt[(i, j)] = maxv
            return maxv
        
        return max(recur(i, j) for i in range(m) for j in range(n))
            