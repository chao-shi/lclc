class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def longest_palin_prefix(s):
            maxsub = 0
            for j in range(len(s) + 1):
                li, hi = 0, j - 1
                while li < hi and s[li] == s[hi]:
                    li, hi = li + 1, hi - 1
                if li >= hi:
                    maxsub = j
            return maxsub
        
        longest_prefix = longest_palin_prefix(s)
        return s[longest_prefix:][::-1] + s
                    