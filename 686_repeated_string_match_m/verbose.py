class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        n, m = len(A), len(B)
        
        # A repeat K times, there are at most n kinds of substr with length m
        # There are n kinds if 
        # 1 + (k - 1) * n >= m
        # k >= (m + n -1) / n
        # larger than that, no need to check since no more new substr
        
        max_k = int(math.ceil(float(m + n - 1) / float(n)))
        min_k = m / n 
        for k in range(min_k, max_k + 1):
            Ak = A * k
            if B in Ak:
                return k
        return -1
    
# Actually max_k is always min_k + 2
# see main.py