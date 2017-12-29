class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # m[i][j] stores if s[i:j] is palindrome
        m = [[False] * (len(s) + 1) for i in range(len(s) + 1)]

        maxstr = ""
        for i in range(len(s) + 1):
            m[i][i] = True
        for i in range(len(s)):
            m[i][i+1] = True
            maxstr = s[i]

        for diff in range(2, len(s) + 1):
            i, j = 0, diff
            while j <= len(s):
                if s[i] == s[j-1]:
                    m[i][j] = m[i+1][j-1]
                
                if m[i][j] and j - i > len(maxstr) :
                    maxstr = s[i:j]
                
                i, j = i + 1, j + 1 

        return maxstr

# passes OJ 6789 ms