class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        # for example n = 24, remain_n = 4, factors = [2, 3]
        # factors increasing seq
        def recur(remain_n, factors):
            if len(factors) > 0:
                res.append(factors + [remain_n])

            factor_start = 2 if len(factors) == 0 else factors[-1]
            for first_factor in xrange(factor_start, int(math.sqrt(remain_n)) + 1):
                if remain_n % first_factor == 0:
                    recur(remain_n / first_factor, factors + [first_factor])  

        recur(n, [])
        return res

# Why do you think this recursion does not have the problem of recomputing.
# The help of factors