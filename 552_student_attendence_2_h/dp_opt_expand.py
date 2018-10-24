class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mt = {}
        mod = 10 ** 9 + 7
        
        for A in range(2):
            a = b = c = d = e = f = 1
                
        for k in xrange(n):
            a, b, c, d, e, f = (c, (a + c) % mod, (b + c) % mod,
                                (c + f) % mod, (c + d + f) % mod, (c + e + f) % mod)
        
        return f