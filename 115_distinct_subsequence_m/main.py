class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
        for i in range(len(s) + 1):
            m[i][0] = 1
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    m[i][j] += m[i-1][j-1]
                m[i][j] += m[i-1][j]
        return m[len(s)][len(t)]