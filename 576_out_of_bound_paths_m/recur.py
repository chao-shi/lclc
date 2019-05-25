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
        def out(x, y):
            return x < 0 or y < 0 or x >= m or y >= n

        def recur(x, y, step):
            if out(x, y):
                return 1
            elif step == 0:
                return 0
            elif (x, y, step) in mt:
                return mt[(x, y, step)]
            else:
                total = 0
                for v in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    total = (total + recur(x+v[0], y+v[1], step-1)) % mod
                mt[(x, y, step)] = total 
                return total
            
        mt = {}
        return recur(i, j, N)