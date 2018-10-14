class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.m, self.n = n_rows, n_cols
        self.replace_map = {}
        self.total_0 = self.m * self.n

    def flip(self):
        """
        :rtype: List[int]
        """
        idx = random.randint(0, self.total_0 - 1)
        
        real_idx = self.replace_map.get(idx, idx)

        self.replace_map[idx] = self.replace_map.get(self.total_0 - 1, self.total_0 - 1)
            
        self.total_0 -= 1
        return [real_idx / self.n, real_idx % self.n]
        

    def reset(self):
        """
        :rtype: void
        """
        self.replace_map = {}
        self.total_0 = self.m * self.n
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()

# Think about one-d array
# Removing element index i, instead of creating a gap.
# We swap last element here. 
# To save storage, we use a replace_map to store i:last
# However, last index may also in the replace_map,
# Careful line 20