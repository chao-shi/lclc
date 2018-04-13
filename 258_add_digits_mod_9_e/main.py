class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # number abcd and a+b+c+d
        # The different is multiple of 9
        # After each round, the new number has the same mod 9 with origin
        # The final value will be in range of [0, 9]
        # The final value will be the mod of 9 (with 0 mapped to 9 except 0 itself
        res = num % 9
        if res:
            return res
        return 9 if num else 0