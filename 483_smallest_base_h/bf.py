class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        # k is the base and the representation is
        # m bits of 1
        # We then have
        # (k**m - 1) / (k-1) = n
        # m = log_k (n * k - n + 1)
        # m needs to be integer
        n = int(n)
        for k in xrange(2, n):
            exp = math.log(1 + (k - 1) * n, k)
            if exp == int(exp):
                return str(k)
            
# Python log is very inaccurate with float
# math.log(47437928, 362) returns 2.9999999999999996 instead of 3
# Does not pass OJ test case "131407"