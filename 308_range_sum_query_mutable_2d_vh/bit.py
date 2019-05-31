import math
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m, self.n = len(matrix), len(matrix[0]) if matrix else 0
        self.matrix = matrix

        if self.m > 0:
            self.mlen = 2 ** int(math.ceil(math.log(self.m, 2)))
        else:
            self.mlen = 0

        if self.n > 0:
            self.nlen = 2 ** int(math.ceil(math.log(self.n, 2)))
        else:
            self.nlen = 0

        self.bit = [[0] * (self.nlen + 1) for _ in range(self.mlen+1)]
        accu_sum = [[0] * (self.nlen + 1) for _ in range(self.mlen+1)]

        for i in range(1, self.mlen+1):
            for j in range(1, self.nlen+1):
                accu_sum[i][j] = accu_sum[i-1][j] + accu_sum[i][j-1] - accu_sum[i-1][j-1]
                if i - 1 < self.m and j - 1 < self.n:
                    accu_sum[i][j] += self.matrix[i-1][j-1]

        for i in range(1, self.mlen+1):
            for j in range(1, self.nlen+1):
                i_base, j_base = i & (i-1), j & (j - 1)
                self.bit[i][j] = accu_sum[i][j] + accu_sum[i_base][j_base] - accu_sum[i][j_base] - accu_sum[i_base][j]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val

        r = row + 1
        while r <= self.mlen:
            c = col + 1
            while c <= self.nlen:
                self.bit[r][c] += delta
                c += c & (-c)
            r += r & (-r)


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.beginSumRange(row2 + 1, col2 + 1) + self.beginSumRange(row1, col1) - \
            self.beginSumRange(row1, col2+1) - self.beginSumRange(row2+1, col1)
        

    def beginSumRange(self, row, col):
        sumv = 0
        r = row

        while r > 0:
            c = col
            while c > 0:
                sumv += self.bit[r][c]
                c = c & (c-1)
            r = r & (r-1)
        return sumv

# sol = NumMatrix([
#   [3, 0, 1],
#   [5, 6, 3]
# ])

# print sol.sumRegion(0, 1, 1, 2)
# #sumRegion(2, 1, 4, 3) -> 8
# sol.update(1, 2, 2)
# print sol.sumRegion(0, 1, 1, 3)
# #sumRegion(2, 1, 4, 3) -> 10