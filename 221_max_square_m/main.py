class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        memory = [[0] * (n + 1) for i in range(m + 1)]
        max_square = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '1':
                    min_dimen = min(memory[i][j-1], memory[i-1][j])
                    memory[i][j] = min_dimen
                    if matrix[i-1-min_dimen][j-1-min_dimen] == "1":
                        memory[i][j] += 1
                max_square = max(max_square, memory[i][j])
        return max_square ** 2
        