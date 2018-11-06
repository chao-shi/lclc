class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(0, int(math.sqrt(c / 2)) + 1):
            b = math.sqrt(c - a**2)
            if int(b) ** 2 + a ** 2 == c:
                return True
        return False