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
                minv = sys.maxint
                for k in range(i+1, j):
                    minv = min(minv, k + max(m[i][k-1], m[k+1][j]))
                m[i][j] = minv
        return m[1][n]

# line 17, in the case of of solving problem P(i, j) where we need to find the pivot, 
# and split to two half problems. P(i, k-1) and P(k+1, j)
# By problem definition we have i <= j
# To make P(i, k-1) and P(k+1, j) both to be valid problem

# The diff between i, j must be at least 2 !!!
# diff 1 is base case