class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = [[0] * (n + 1) for i in range(n+1)]
        for j in range(2, n + 1):
            m[j-1][j] = j-1
            for i in range(j - 2, 0, -1):
                m[i][j] = min([k + max(m[i][k-1], m[k+1][j]) for k in range(i+1, j)])
        return m[1][n]

# Easier to write without diff
# j always move to the right. 
# i starts left to j and move left 