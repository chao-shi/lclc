class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = [0, 0]
        for i in range(1, len(s)):
            if s[i] == ')' and s[i-1] == '(':
                m.append(m[i-1] + 2)
            elif s[i] == ')':
                # ((???)) first element is j index
                j = i - m[i] - 1
                if j >= 0 and s[j] == '(':
                    m.append(m[i] + 2 + m[j])
                else:
                    m.append(0)
            else:
                m.append(0)
        return max(m)
    
# careful line 15, need to add m[j]