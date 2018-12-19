class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                p, q = i, i + 1
                while p >= 0 and q < len(s) and s[p] == s[i] and s[q] == s[i+1]:
                    p, q = p - 1, q + 1
                cnt += (q - p - 1) / 2
        return cnt                
    
# Still linear, each seg will be counted at most twice