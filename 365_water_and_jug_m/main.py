from fractions import gcd
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # z = ax + by
        # z <= x + y skip the case x, y = 0
        return z == 0 or (z <= x + y and z % gcd(x, y) ==0)