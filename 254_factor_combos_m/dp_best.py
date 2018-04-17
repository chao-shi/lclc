class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = {}
        divisors = [i for i in xrange(1, int(math.sqrt(n)) + 1) if n % i == 0]
        divisors += [n / d for d in divisors if n / d != d][::-1]
        for i in divisors:
            res_i = []
            for first_factor in xrange(2, int(math.sqrt(i)) + 1):
                if i % first_factor != 0:
                    continue
                res_i.extend([first_factor] + combo for combo in m[i / first_factor] if first_factor <= combo[0])
                res_i.append([first_factor, i / first_factor])
            m[i] = res_i
        return m[n]

# beats 100%, improved from dp.py