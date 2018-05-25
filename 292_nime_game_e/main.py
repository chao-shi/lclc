class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = [True] * 3
        for i in xrange(4, n+1):
            newv = any(r is False for r in res)
            res = res[1:] + [newv]
        return res[-1]