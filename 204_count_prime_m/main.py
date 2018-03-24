class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True] * n
        cnt = 0
        for i in range(2, n):
            if primes[i]:
                j = 2 * i
                while j < n:
                    primes[j] = False
                    j += i
                cnt += 1
        return cnt

# Counting while computing
# NlogN
# logN from Sigma(1/n)