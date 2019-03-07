class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = []
        def recur(root):
            if root > n:
                return
            elif len(res) >= k:
                return
            if root != 0:
                res.append(root)
            nexts = range(10) if root != 0 else range(1, 10)
            for i in nexts:
                recur(root * 10 + i)
        recur(0)
        return res[k]

# TLE, enumerate does not work for large numbers