class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        start_indexes = map(lambda x:(0, x), range(n)) + map(lambda x:(x, 0), range(1, m))
        
        for i, j in start_indexes:
            ii, jj = i + 1, j + 1
            while ii < m and jj < n and matrix[ii][jj] == matrix[i][j]:
                ii, jj = ii + 1, jj + 1
            if ii < m and jj < n:
                return False
        return True
                