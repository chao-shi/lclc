class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        m[0][0] = True
        
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                m[0][i] = m[0][i-2]
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '.':
                    m[i][j] = m[i][j] or m[i-1][j-1]
                elif p[j-1] == '*':
                    m[i][j] = m[i][j] or m[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        m[i][j] = m[i][j] or m[i-1][j]
                elif p[j-1] == s[i-1]:
                    m[i][j] = m[i][j] or m[i-1][j-1]
        return m[len(s)][len(p)]

# Why it is better to put each key char in each condition
# In the future, what if reg includes "\.", then line 21 and line 23 needs to strip the escape
# Therefore it is not good to merge line 23 with line 17