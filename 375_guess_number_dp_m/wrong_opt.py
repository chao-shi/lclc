class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # (cost, number of guesses)
        res = [(0, 0), (0, 0), (1, 1)]
        # if (1, i) uses (C, N)
        # Then (k, k + i - 1) uses C + N *(k - 1) since each number is 1-1 mapping
        
        def cost_map(i, j, res):
            if i > j:
                return 0
            n = j - i + 1
            return res[n][0] + res[n][1] * (i - 1)
        
        def step_map(i, j, res):
            if i > j:
                return 0
            n = j - i + 1
            return res[n][1]

        for i in range(3, n + 1):
            min_tuple = (sys.maxint, sys.maxint)
            for j in range(1, i + 1):
                tuple_left = (cost_map(1, j-1, res), step_map(1, j-1, res))
                tuple_right = (cost_map(j+1, i, res), step_map(j+1, i, res))
                tuple_both = max(tuple_left, tuple_right)
                tuple_both = (tuple_both[0] + j, tuple_both[1] + 1)
                min_tuple = min(min_tuple, tuple_both)
            res.append(min_tuple)
        return res[n][0]

# Only one problem here, problem (i, j) can be mapped to (1, j - (i-1))
# This trick is not correct. 
# (i, j) does not always follow whatever optimal (1, j - i +1) does
# may tradeoof the number of steps. Pick one with higher base cost but fewer steps