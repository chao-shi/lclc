class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        for i in range(len(s)):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j == len(t):
                return False
            j += 1
        return True