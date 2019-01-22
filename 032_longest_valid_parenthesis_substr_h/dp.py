class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = [0] * (len(s) + 1)
        for i in range(1, len(s)):
            if s[i] == ')':
                j = i - m[i] - 1
                if j >= 0 and s[j] == '(':
                    m[i+1] = m[i] + 2 + m[j]
                    continue
            m[i + 1] = 0
        print m
        return max(m)

# j >= 0 check required
# careful line 12, need to add m[j]