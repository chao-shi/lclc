class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = set([1])
        res = []

        while len(res) < n:
            minv = min(s)
            res.append(minv)
            s.remove(minv)
            s.add(minv * 2)
            s.add(minv * 3)
            s.add(minv * 5)

        return res[-1]
            
# Somehow set passes, but still not optimal