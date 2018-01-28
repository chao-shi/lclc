class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        c = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or c > 0:
            if i >= 0:
                c += int(a[i])
            if j >= 0:
                c += int(b[j])
            res.append(c % 2)
            c /= 2
            i, j = i - 1, j - 1
        return "".join(map(str, res[::-1]))
        