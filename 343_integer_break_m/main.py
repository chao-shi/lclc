class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.mt = {}
        def recur(n):
            if n in self.mt:
                return self.mt[n]
            elif n < 2:
                return 0
            # suppose the split is sorted
            # We iterate on the first in split
            # it is no bigger than half
            max_p = n - 1
            for i in range(1, n/2 + 1):
                max_p = max(max_p, i * (n - i), i * recur(n - i))
            self.mt[n] = max_p
            return max_p
        
        return recur(n)