class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        # Careful
        def direct_out(i, j):
            res = 0
            if i == 0:
                res += 1
            if i == m - 1:
                res += 1
            if j == 0:
                res += 1
            if j == n - 1:
                res += 1
            return res

        x, y = i, j
        res = [[0] * n for i in range(m)]
        
        for k in range(1, N+1):
            new_res = [[0] * n for i in range(m)]

            for i in range(m):
                for j in range(n):
                    # Careful here
                    total = direct_out(i, j) 
                    if i > 0:
                        total += res[i-1][j]
                    if j > 0:
                        total += res[i][j-1]
                    if i < m - 1:
                        total += res[i+1][j]
                    if j < n - 1:
                        total += res[i][j+1]
                    new_res[i][j] = total % mod
            res = new_res
        return res[x][y] % mod
    
# Careful about base case line 33 and 4 direction
        