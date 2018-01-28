class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # f(k) = k ^ 2 - x
        # find f(k) = 0
        k = x
        while True:
            sqrt = int(k)
            if sqrt ** 2 <= x:
                return sqrt
            k -= (k ** 2 - x) / (2.0*k)

# First bad versio easier