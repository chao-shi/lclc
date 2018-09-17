class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # KMP algorithm
        # longest proper prefix suffix map
        def make_lps(s):
            lps = [0] * len(s)
            for i in range(1, len(s)):
                len_cand = lps[i-1]
                while s[len_cand] != s[i]:
                    if len_cand == 0:
                        len_cand = -1
                        break
                    else: 
                        len_cand = lps[len_cand - 1]
                lps[i] = len_cand + 1
            return lps
        
        lps = make_lps(s)
        p_len = lps[-1]
        
        # if S is k of substring pattern p
        # then p_len will be (k - 1) * p here
        return p_len > 0 and len(s) % (len(s) - p_len) == 0

# Inspired by discussions