class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        res = [[0] * n for i in range(m)]
        MAX = m * n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    res[i][j] = min((res[i-1][j] + 1 if i > 0 else MAX), (res[i][j-1] + 1 if j > 0 else MAX))
                    
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 1:
                    res[i][j] = min(res[i][j], (res[i+1][j] + 1 if i < m-1 else MAX), (res[i][j+1] + 1 if j < n-1 else MAX))
        return res
    
# Doubtful about the solution. But it passes OJ
# How to solve the DP problems where there is loop between problem and subproblem in general?