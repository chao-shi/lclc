# Only work for positives
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        c = 0
        mask = 1
        res = 0
        while a > 0 or b > 0 or c > 0:
            ad = a & 1
            bd = b & 1
            r, cc = ad ^ bd, ad & bd
            r, c = r ^ c, cc | r & c
            if r == 1:
                res |= mask
            a, b, mask = a >> 1, b >> 1, mask << 1
        return res