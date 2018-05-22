# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lb, hb = 0, n - 1
        while lb <= hb:
            mid = (lb + hb) / 2
            if isBadVersion(mid):
                hb = mid - 1
            else:
                lb = mid + 1
        return lb