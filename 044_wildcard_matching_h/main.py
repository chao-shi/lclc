class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = [[False] * (len(p) + 1) for i in range(1 + len(s))]
        
        m[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == "*":
                m[0][i] = m[0][i-1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i-1] == p[j-1]:
                    m[i][j] = m[i][j] or m[i-1][j-1]
                elif p[j-1] == '?':
                    m[i][j] = m[i][j] or m[i-1][j-1]
                elif p[j-1] == '*':
                    m[i][j] = m[i][j] or m[i][j-1] or m[i-1][j]
        return m[len(s)][len(p)]

# Read more carefully. * not a * here 