class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_mirror = s[::-1]
        i, j = 0, 0
        n = len(s)
        while i < n:
            if s[i] == s_mirror[i]:
                i += 1
            else:
                # Try delete s[i] or s_mirror[i], which is also s[n - i - 1]
                return s[i+1:] == s_mirror[i:n-i-1] + s_mirror[n-i:] or s[i:n-i-1] + s[n-i:] == s_mirror[i+1:]
        return True