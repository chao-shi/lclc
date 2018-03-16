class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        base5 = 5
        cnt = 0
        while n >= base5:
            cnt += n / base5
            base5 *= 5
        return cnt