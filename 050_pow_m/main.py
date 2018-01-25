class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = n < 0
        if flag:
            n = -n
        
        def pow(x, n):
            if n == 0:
                # better 1.0 here
                return 1.0
            elif n % 2 == 1:
                half = pow(x, n/2)
                return half * half * x
            else:
                half = pow(x, n/2)
                return half * half
        
        res = pow(x, n)
        if flag:
            return 1.0/res
        return res