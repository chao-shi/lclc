class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix[0]) == 0:
            return

        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(e == 0 for e in matrix[0])
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_zero:
            for i in range(n):
                matrix[0][i] = 0
        
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0