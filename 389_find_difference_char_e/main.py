from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnts, cntt = Counter(s), Counter(t)
        for ch in cntt:
            if cntt.get(ch) != cnts.get(ch, 0):
                return ch
        