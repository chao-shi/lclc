class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        base2 = 1
        while n - m  >= base2:
            base2 <<= 1
        return (m & ~(base2 - 1)) & (n & ~(base2 - 1))

# Line 11 make last few digits zero keep the rest