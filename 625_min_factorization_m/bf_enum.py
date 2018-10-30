class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        self.minv = None
        def recur(remain, cur):
            if self.minv != None and cur > self.minv:
                return 
            elif cur > (1 << 31) - 1:
                return 
            elif remain == 1:
                self.minv = cur if self.minv == None else min(self.minv, cur)
            else:
                for d in range(9, 1, -1):
                    if remain % d == 0:
                        recur(remain / d, cur * 10 + d)

        if a == 1:
            return 1

        recur(a, 0)
        return self.minv if self.minv != None else 0