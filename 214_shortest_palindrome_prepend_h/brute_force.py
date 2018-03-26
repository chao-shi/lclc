class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def longest_palin_prefix(s):
            i, j = 0, 0
            maxsub = 0
            while j < len(s):
                li, ri = i, j
                while li >= 0 and ri < len(s) and s[li] == s[ri]:
                    li, ri = li - 1, ri + 1
                
                if li < 0:
                    maxsub = max(maxsub, ri - li - 1)
                
                if i == j:
                    j += 1
                else:
                    i += 1
            return maxsub
        
        longest_prefix = longest_palin_prefix(s)
        return s[longest_prefix:][::-1] + s
                    