class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach 1
        sr = s[::-1]
        n = len(s)
        m = [[0] * (n+1) for i in range(n+1)]
        maxpalinlen = 0
        maxpalin = None
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == sr[j-1]:
                    m[i][j] = m[i-1][j-1] + 1
                if j + (i - m[i][j]) == n:
                    # find a palindrome
                    if m[i][j] > maxpalinlen:
                        maxpalinlen = m[i][j]
                        maxpalin = s[i-m[i][j]:i]
        return maxpalin
                    

# m[i][j] stores lenght longest common substring 
# s[i - m[i][j]: i] and sr[j - m[i][j] : j] are the same
# This satisfy the reflection of palindrome
# next check index on line 17