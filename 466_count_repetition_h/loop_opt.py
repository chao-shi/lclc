class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        i, j = 0, 0
        hm = {}
        while i < n1 * len(s1):
            if j % len(s2) == 0 and j > 0:
                if i % len(s1) in hm:
                    i1, j1 = hm[i % len(s1)]
                    mul = (n1 * len(s1) - i1) / (i - i1)
                    i += (mul - 1) * (i - i1)
                    j += (mul - 1) * (j - j1)
                # Only set first time
                else:
                    hm[i % len(s1)] = (i, j)
            ch1 = s1[i % len(s1)]
            ch2 = s2[j % len(s2)]
            if ch1 == ch2:
                i, j = i + 1, j + 1
            else:
                i += 1
        
        rep_s2 = j / len(s2)
        return rep_s2 / n2

# Generalize the repeating pattern where it does not start with segments of S1
# 
# --------------------------------------------------------------------------------
# n1 * s1             | i1 |                                          |i|
# S2                  | j1 |                                          |j|
# ---------------------------------------------------------------------------------
# 
# |                                 |                                           |
# S1 start                         S1 start                                  S1 start
# 
# Detecting the repeating pattern, when j % len(s2) == 0 (line 13)
# When first time i, j, set hm in block 20
# when next time we saw i, j such that i % len(s1) in hm, retrieve i1, j1
# 
# mul is how many (i - i1) can be fit.
# airlift i, j accordingly to the end.
# continue the loop.
# 
# The beauty of this method is that after airlift happens, we can still run the block 13 logic again,
# This case mul will be 1 and no airlifting happens