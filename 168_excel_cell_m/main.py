class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = []
        while n > 0:
            idx = n % 26
            if idx == 0:
                idx = 26
            ret.append(chr(ord('A') + idx - 1))
            n = (n - idx) / 26
        return "".join(ret[::-1])
            