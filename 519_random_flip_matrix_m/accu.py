class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        # make it flat shape
        self.m, self.n = min(n_rows, n_cols), max(n_rows, n_cols)
        self.invert = self.m != n_rows

        self.accu_0 = [i * self.n for i in range(self.m + 1)]
        self.cnt_0 = self.m * self.n
        self.matrix = [[0] * self.n for i in range(self.m)]
        

    def flip(self):
        """
        :rtype: List[int]
        """
        r = random.randint(0, self.cnt_0 - 1)
        i = bisect.bisect_right(self.accu_0, r) - 1
        r -= self.accu_0[i]        
        j = [jj for jj in range(self.n) if self.matrix[i][jj] == 0][r]

        self.matrix[i][j] = 1
        for ii in range(i + 1, self.m + 1):
            self.accu_0[ii] -= 1
        self.cnt_0 -= 1
        
        ret = [i, j] if not self.invert else [j, i]
        return ret
        
    def reset(self):
        """
        :rtype: void
        """
        self.accu_0 = [i * self.n for i in range(self.m + 1)]
        self.cnt_0 = self.m * self.n
        self.matrix = [[0] * self.n for i in range(self.m)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
# 
# MLE