# 1622ms supposed to be slow
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        limit = k
        n, m = len(matrix), len(matrix[0])
        
        if n > m:
            matrix = [[matrix[i][j] for i in range(n)] for j in range(m)]
            n, m = m, n

        sums = [[0] * (m+1) for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                sums[i+1][j+1] = matrix[i][j] + sums[i+1][j] + sums[i][j+1] - sums[i][j]

        maxv = None
        diffs = [[[0] for j in range(n+1)] for i in range(n+1)]
        for k in range(m):
            for i in range(n):
                for j in range(i, n):
                    # sums[j+1][k+1] - sums[i][k+1] - x <= limit
                    idx = bisect.bisect_left(diffs[i][j+1], sums[j+1][k+1] - sums[i][k+1] - limit)
                    if idx < len(diffs[i][j+1]):
                        cand = sums[j+1][k+1] - sums[i][k+1] - diffs[i][j+1][idx]
                        maxv = max(maxv, cand) if maxv != None else cand
                    
                    idx = bisect.bisect_left(diffs[i][j+1], sums[j+1][k+1] - sums[i][k+1])
                    diffs[i][j+1].insert(idx, sums[j+1][k+1] - sums[i][k+1])
        return maxv