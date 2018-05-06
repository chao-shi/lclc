class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        factors = [2, 3, 5]
        idx = [0, 0, 0]
        res = [1]

        for i in range(n-1):
            for j in range(len(factors)):
                while res[idx[j]] * factors[j] <= res[-1]:
                    idx[j] += 1
            res.append(min(factors[j] * res[idx[j]] for j in range(len(idx))))
        return res[-1]