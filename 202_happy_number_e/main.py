class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next(n):
            ret = 0
            while n > 0:
                ret += (n % 10) ** 2
                n /= 10
            return ret
        
        sp, fp = n, n
        while fp != 1:
            fp = next(next(fp))
            sp = next(sp)
            if sp == fp:
                break
        return fp == 1