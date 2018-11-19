class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        res = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                neigh = []
                for v in [(0, 0), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
                    ii, jj = i + v[0], j + v[1]
                    if 0 <= ii < m and 0 <= jj < n:
                        neigh.append(M[ii][jj])
                res[i][j] = sum(neigh) / len(neigh)
        return res