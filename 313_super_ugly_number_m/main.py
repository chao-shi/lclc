class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        res = [1]
        idx = [0] * k
        
        while len(res) < n:
            res.append(min(res[idx[i]] * primes[i] for i in range(len(idx))))
            for i in range(len(idx)):
                if res[-1] == res[idx[i]] * primes[i]:
                       idx[i] += 1
        return res[-1]
        
# Search for 264 ugly number, a simple generalization.