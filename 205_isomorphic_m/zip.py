class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        z = zip(s, t)
        z = sorted(z)
        for i in range(1, len(s)):
            if z[i][0] == z[i-1][0] and z[i][1] != z[i-1][1]:
                return False
        
        z = sorted(z, key=lambda x:x[1])
        for i in range(1, len(s)):
            if z[i][1] == z[i-1][1] and z[i][0] != z[i-1][0]:
                return False
            
        return True