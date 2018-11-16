class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = [0, 1, 2, 3]
        for i in range(4, N+1):
            maxv = 1 + res[-1]
            # We only multiply by 2, 3, 4, 5
            for j in range(max(0, i - 6), i - 2):
                # step j ... i - 1 does A, C, P, P ....
                maxv = max(maxv, res[j] * (i - j - 1))
            res.append(maxv)
        return res[N]

# Math trick: Never needs to multiply by more than 5
# Multiply by 6, instead of having ACVVVVV, we should do ACVACVV