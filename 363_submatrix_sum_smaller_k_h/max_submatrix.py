# only partial solution. 
# max submatrix ignoring k here
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n, m = len(matrix), len(matrix[0])
        
        sums = [[0] * (m+1) for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                sums[i+1][j+1] = matrix[i][j] + sums[i+1][j] + sums[i][j+1] - sums[i][j]

        maxv = -sys.maxint
        minm = [[0] * (n+1) for i in range(n+1)]
        for k in range(m):
            for i in range(n):
                for j in range(i, n):
                    maxv = max(maxv, sums[j+1][k+1] - sums[i][k+1] - minm[i][j+1])
                    minm[i][j+1] = min(minm[i][j+1], sums[j+1][k+1] - sums[i][k+1])
        return maxv

# N^2 for smaller dimension. Complexity is n^2 * m if n < m
# Good to use double array then hash map
# line 21 j starts from i. 
# Store sum using +1 index, but iterating by elements. This is cleaner
# First column initialization