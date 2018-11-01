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
        
        for i in xrange(2, n + 1):
            nv = [1] + [0] * k
            # Keep a sliding window of at most i
            win_sum = 0
            
            for j in xrange(k + 1):
                if j > (i - 1) * i / 2:
                    break

                win_sum = (win_sum + v[j]) % mod
                if j - i >= 0:
                    win_sum = (win_sum - v[j - i]) % mod
                nv[j] = win_sum % mod
            v = nv
        return v[-1]

# Optimize with cumulative sum