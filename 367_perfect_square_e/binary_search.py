# 25ms
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # first element e such that e * e >= num
        li, hi = 0, num
        while li <= hi:
            mid = (li + hi) / 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                hi = mid - 1
            else:
                li = mid + 1
        return False