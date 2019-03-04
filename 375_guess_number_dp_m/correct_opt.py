class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = [[0] * (n + 1) for i in range(n+1)]
        
        for i in range(1, n):
            m[i][i+1] = i

        for diff in range(2, n):
            for i in range(1, n - diff + 1):
                j = i + diff
                minv = j + m[i][j-1]
                for k in range((i+j)/2, j):
                    minv = min(minv, k + max(m[i][k-1], m[k+1][j]))
                m[i][j] = minv
        return m[1][n]

# 16 choose k from (i+j) / 2
# Not sure if this is right????