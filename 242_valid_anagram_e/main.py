class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnts = collections.Counter(s)
        cntt = collections.Counter(t)
        return cnts == cntt

# OK to compare counter object