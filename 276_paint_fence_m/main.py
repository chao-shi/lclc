class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        last_2_same, last_2_diff = k, k * (k - 1)
        for i in range(n - 2):
            last_2_same, last_2_diff = last_2_diff, (last_2_same + last_2_diff) * (k - 1)
        return last_2_same + last_2_diff