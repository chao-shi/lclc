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
        
# Not faster, this question is not to return one possible combination so line 15 has no way to terminate early
# recur(n) will always call recur(n-1), same as DP