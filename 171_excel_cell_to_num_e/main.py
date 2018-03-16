class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for ch in s:
            idx = ord(ch) - ord('A') + 1
            ret *= 26
            ret += idx
        return ret