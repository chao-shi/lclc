class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 10**9 + 7
        # Last element has choice of 0, 1, .... i - 1
        # C(i, j) = sum(C(i-1, j) + C(i-1, j-1) +... C(i-1, max(0, j - i + 1)))
        # C(n, k) = 0 if k > (n-1)n/2
        
        v = [1] + [0] * k
        
        for i in range(2, n + 1):
            nv = [1] + [0] * k
            for j in range(1, k + 1):
                if j > (i - 1) * i / 2:
                    break
                nv[j] = sum(v[max(0, j + 1 - i):j+1]) % mod
            v = nv
        return v[-1]

print Solution().kInversePairs(1000, 1000)