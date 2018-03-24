class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        m1, m2 = {}, {}
        for i in range(len(s)):
            if s[i] in m1:
                if m1[s[i]] != t[i]:
                    return False
            elif t[i] not in m2:
                m1[s[i]] = t[i]
                m2[t[i]] = s[i]
            else:
                return False
        return True