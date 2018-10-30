class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
       
        if a == 1:
            return 1
        
        # Factorize into 2-9
        factors = []
        remain = a
        for d in range(9, 1, -1):
            while remain % d == 0:
                remain /= d
                factors.append(d)
        
        if remain > 1:
            return 0
        
        factors = factors[::-1]
        ans = 0
        for d in factors:
            ans = ans * 10 + d
            if ans > (1 << 31) - 1:
                return 0
        return ans