class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = [0, 1, 2, 3]
        for i in range(4, N+1):
            maxv = 1 + res[-1]
            for j in range(1, i - 2):
                # step j ... i - 1 does A, C, P, P ....
                maxv = max(maxv, res[j] * (i - j - 1))
            res.append(maxv)
        return res[N]
        