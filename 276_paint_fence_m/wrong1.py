class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        res = [1, k, k*k]
        while len(res) < n + 1:
            res.append(k*(res[-1] - res[-3]))
        return res[-1]
            