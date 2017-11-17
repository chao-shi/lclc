class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod = 1
        for digit in b:
            f = mod
            for i in range(9):
                mod = (mod * f) % 1337
            for i in range(digit):
                mod = (mod * a) % 1337
        return mod

# I thought using loop detection algorithm before, but this is simpler

# Note that line 11 is 9. We need to multiply additional 9 to make it power of 10