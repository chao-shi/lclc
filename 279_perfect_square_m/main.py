import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == int(math.sqrt(n)) ** 2:
            return 1

        mt = [0] * (n + 1)
        
        for i in range(1, n+1):
            mt[i] = min(1 + mt[i - j * j] for j in range(1, int(math.sqrt(i)) + 1))
        return mt[-1]
