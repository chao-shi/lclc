class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.m, self.n = n_rows, n_cols
        self.matrix = ["0" * self.n for i in range(self.m)]
        

    def flip(self):
        """
        :rtype: List[int]
        """
        while True:
            r = random.randint(0, self.m * self.n - 1)
            i, j = r / self.n, r % self.n
            if self.matrix[i][j] == "0":
                self.matrix[i] = self.matrix[i][:j] + "1" + self.matrix[i][j+1:]
                return [i, j]
        

    def reset(self):
        """
        :rtype: void
        """
        self.matrix = ["0" * self.n for i in range(self.m)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()