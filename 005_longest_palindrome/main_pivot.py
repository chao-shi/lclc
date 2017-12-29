class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, 0
        maxstr = ""
        
        while j < len(s):
            ii, jj = i, j
            while ii >=0 and jj < len(s) and s[ii] == s[jj]:
                ii, jj = ii - 1, jj + 1
            if jj -ii - 1 > len(maxstr):
                maxstr = s[ii+1:jj]
            
            if i == j:
                j += 1
            else:
                i += 1
        return maxstr

# Pivot worst case O(N^2), OJ better performer