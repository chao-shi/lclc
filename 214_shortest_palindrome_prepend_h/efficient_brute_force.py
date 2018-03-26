class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def longest_palin_prefix(s):
            r = s[::-1]
            maxsub = 0
            for j in range(len(s) + 1):
                if s.startswith(r[len(s) - j:len(s)]):
                    maxsub = j
            return maxsub
        
        longest_prefix = longest_palin_prefix(s)
        return s[longest_prefix:][::-1] + s

# Start with is faster