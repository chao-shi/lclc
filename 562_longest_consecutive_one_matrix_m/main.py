class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0

        m, n = len(M), len(M[0])
        
        def search_along(i, j, v):
            cnt = 0
            while 0 <= i < m and 0 <= j < n and M[i][j] == 1:
                cnt += 1
                i, j = i + v[0], j + v[1]
            return cnt
                
        max_l = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    if j == 0 or M[i][j-1] == 0:
                        max_l = max(max_l, search_along(i, j, (0, 1)))
                    if i == 0 or M[i-1][j] == 0:
                        max_l = max(max_l, search_along(i, j, (1, 0)))
                    if i == 0 or j == 0 or M[i-1][j-1] == 0:
                        max_l = max(max_l, search_along(i, j, (1, 1)))
                    # Don't forget anti-diagonal
                    if i == m - 1 or j == 0 or M[i+1][j-1] == 0:
                        max_l = max(max_l, search_along(i, j, (-1, 1)))
                    
        return max_l
                    
# Linear, each inner point in segment will only be check once, one point can belong to at most 4 segments
# BF is good enough