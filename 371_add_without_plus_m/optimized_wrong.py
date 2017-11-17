# This is wrong implentation for negative numbers
# in python
# -1 ^ 1 = -2 (not 0) because -1 assume infinite 1 prefixing.
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b > 0:
            a, b = a ^ b, (a & b) << 1
        return a

print Solution().getSum(-1, 1)