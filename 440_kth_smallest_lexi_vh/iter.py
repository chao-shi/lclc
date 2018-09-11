class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        num = 1
        for i in xrange(k-1):
            if num * 10 <= n:
                num = num * 10
            else:
                if num + 1 <= n:
                    num = num + 1
                else:
                    num = num / 10 + 1
                while num % 10 == 0:
                    num = num / 10
        return num