class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        plus = 1
        for i in range(n):
            res = res + [e + plus for e in res[::-1]]
            plus <<= 1
        return res

# Line 11 cannot separate << with =
# a << = 1 is wrong !!