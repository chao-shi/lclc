class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = set(range(2, n))
        for i in range(2, n, 1):
            if i in primes:
                j = 2 * i
                while j < n:
                    if j in primes:
                        primes.remove(j)
                    j += i
        return len(primes)

# Does not pass OJ memory limit