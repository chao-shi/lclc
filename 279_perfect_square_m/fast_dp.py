import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        mt = {}
        def recur(n):
            if n in mt:
                return mt[n]
            elif n == 0:
                return 0
            else:
                mt[n] = min(1 + recur(n - i * i) for i in range(int(math.sqrt(n)), 0, -1))
                return mt[n] 
        
        return recur(n)
        
# In theory will be faster in early pruning, but also expensive in stack calls
# But OJ is slower with 7000+ ms.
# Slower than main.py