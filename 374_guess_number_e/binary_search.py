# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        li, hi = 1, n
        while li <= hi:
            mid = (li + hi)/2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans > 0:
                li = mid + 1
            else:
                hi = mid - 1
        