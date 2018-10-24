class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mt = {}
        
        for A in range(2):
            for L in range(3):
                mt[(A, L)] = 1
                
        for k in range(1, n+1):
            mt_next = {}
            for A in range(2):
                for L in range(3):
                    res = 0
                    if A > 0:
                        res += mt[(A - 1, 2)]
                    if L > 0:
                        res += mt[(A, L-1)]
                    res += mt[(A, 2)]
                    mt_next[(A, L)] = res
            mt = mt_next
        
        return mt[(1, 2)] % (10 ** 9 + 7)

print Solution().checkRecord(100000)
# Still slow