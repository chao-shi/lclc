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
                    
                
                for k in range(1, j - i):
                    if (j - i) % k != 0:
                        continue
                    reps = (j - i) / k
                    rep_str = s[i:i+k] * reps
                    
                    if rep_str != s[i:j]:
                        continue
                    
                    encoded = str(reps) + "[" + mt[(i, i+k)] + "]"
                    mt[(i, j)] = shorter(mt[(i, j)], encoded)
        
        return mt[(0, len(s))]
                    
                
                    
# Got inspired by length no longer than 160. BF is Ok