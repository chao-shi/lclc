class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        flag = 1 if n % 2 == 0 else -1
        res = 0
        term = 1
        for k in xrange(n + 1):
            res = (res + flag * term) % mod
            flag = -flag
            term = (term * (n - k)) % mod 
        return res

# Main idea, set intersection calculation
# A V B = A + B - A^B
# A V B V C = A + B + C - A^B - A^C - B^C + A^B^C

# P(N) = N! - C(N, 1) * (N-1)! + C(N, 2) * (N-2)! .... +/- 1
# Explaination: all perms - at_least_1_violation + at_least_2_violation
# P(N) = sig((-1) ** k * C(N, k) * (N-K)!) = sig((-1) ** k * N * N-1 * ... N-k+1)