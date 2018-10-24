class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.mt = {}
        # A: number of A available
        # L: number of leading L prefix allowed
        def recur(k, A, L):
            if k == 0:
                return 1
            
            if (k, A, L) in self.mt:
                return self.mt[(k,A,L)]

            res = 0
            if A > 0:
                res += recur(k-1, A - 1, 2)
            if L > 0:
                res += recur(k-1, A, L - 1)
            res += recur(k-1, A, 2)
            self.mt[(k,A,L)] = res
            return res
        
        return recur(n, 1, 2) % (10 ** 9  + 7)
    
print Solution().checkRecord(100000)