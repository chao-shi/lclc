class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None
        
        flag = (dividend >= 0) != (divisor >= 0)
        dividend, divisor = abs(dividend), abs(divisor)
            
        multiplier = 1
        while divisor <= dividend:
            divisor <<= 1
            multiplier <<= 1
        divisor >>= 1
        multiplier >>= 1
        
        q = 0
        while dividend > 0 and multiplier > 0:
            if dividend >= divisor:
                dividend -= divisor
                q += multiplier
            divisor >>= 1
            multiplier >>= 1
            
        q = -q if flag else q
        return max(min((1 << 31) - 1, q), - 1 << 31)

# Line 11, how to make flag quickly
# terminating condition 22
# line 30 for OJ