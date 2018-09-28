class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        chars = S.upper().replace("-", "")
        res = []
        start = len(chars) % K
        if start != 0:
            res.append(chars[:start])
        for i in range(start, len(chars), K):
            res.append(chars[i:i+K])
        return "-".join(res)