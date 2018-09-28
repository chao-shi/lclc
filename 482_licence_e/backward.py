class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        chars = S.replace("-", "")
        res = []
        for i in range(len(chars), 0, -K):
            res.append(chars[max(0, i-K):i])
        return "-".join(map(lambda x:x.upper(), res[::-1]))