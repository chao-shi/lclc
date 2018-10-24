class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mt = {}
        
        for A in range(2):
            for L in range(3):
                mt[(0, A, L)] = 1
                
        for k in range(1, n+1):
            for A in range(2):
                for L in range(3):
                    res = 0
                    if A > 0:
                        res += mt[(k-1, A - 1, 2)]
                    if L > 0:
                        res += mt[(k-1, A, L-1)]
                    res += mt[(k-1, A, 2)]
                    mt[(k, A, L)] = res
        
        return mt[(n, 1, 2)] % (10 ** 9 + 7)