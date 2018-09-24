class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        def shorter(s1, s2):
            return s1 if len(s1) <= len(s2) else s2

        mt = {}
        for l in range(1, len(s) + 1):
            for i in range(len(s) - l + 1):
                j = i + l
                #print i, j
                mt[(i, j)] = s[i:j]
                
                # split into s[i:k] and s[k:j]
                for k in range(i + 1, j):
                    concat = mt[(i,k)] + mt[(k,j)]
                    mt[(i, j)] = shorter(mt[(i, j)], concat)
                    
                ss = s[i:j]
                k = (ss + ss).find(ss, 1)
                if k < len(ss):
                    encoded = "{}[{}]".format(str(len(ss) / k), mt[(i, i + k)])
                    mt[(i, j)] = shorter(mt[(i, j)], encoded)
        
        return mt[(0, len(s))]
                    
                
                    
# Replace block 22 using the logic below
# https://leetcode.com/problems/encode-string-with-shortest-length/discuss/95602/Short-Python
# 
# Difficulty is how to prove the first ss we find on line 23 is optimal.
# 
# Line 23 tries to find the shortest repeating pattern, making the multiplier maximal.
# 
# We assume that we will try to make the pattern as shorter as possible and the number as big as enough
# 2[abab] -> 4[ab], save two places for pattern, number does not grow more than one bit
# 
# Very loose proof though.