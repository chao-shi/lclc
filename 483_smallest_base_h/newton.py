class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        # k is the base and the representation is
        # m bits of 1
        # We then have from math
        # (k**m - 1) / (k-1) = n
        # m = log_k (n * k - n + 1)
        # m needs to be integer
        
        # we know that k = 2 m will be largest
        m_max = int(math.ceil(math.log(1 + int(n), 2)))
        for m in range(m_max, 1, -1):
            # solve high order equation
            # k**m - nk + n - 1 = 0
            
            # Find k using newton approach
            res = self.solve_equation(m, int(n))
            if res != False:
                return str(res)
            

    # k**m - nk + n - 1 = 0
    # TODO: Why newton approach always work here.
    # Hard to prove they are always monotonic
    def solve_equation(self, m, n):
        k_l, k_h = 2, n - 1
        while k_l <= k_h:
            mid = (k_l + k_h) / 2
            val = mid ** m - n * mid + n - 1 
            if val == 0:
                return mid
            elif val < 0:
                k_l = mid + 1
            else:
                k_h = mid - 1
        return False
    

        