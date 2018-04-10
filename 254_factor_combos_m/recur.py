class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = {}
        def recur(n):
            if n in m:
                return m[n]
            m[n] = []
            for first_factor in xrange(2, int(math.sqrt(n)) + 1):
                if n % first_factor != 0:
                    continue
                m[n].extend([first_factor] + combo for combo in recur(n / first_factor) if first_factor <= combo[0])
                m[n].append([first_factor, n / first_factor])
            return m[n]
        return recur(n)

# How can further imporve without using additional memory for number other n ?
# What can be done line the first_factor <= combo[0] comparison on line 15