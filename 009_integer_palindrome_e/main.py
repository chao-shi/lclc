class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        # special case for negative
        # in python -6%10 = 4 -6/10=-1, this makes the integer 
        # opertions hard to track

        # careful don't pollute x
        rev = 0
        xx = x
        while xx > 0:
            rev *= 10
            rev += xx % 10
            xx /= 10
        return rev == x