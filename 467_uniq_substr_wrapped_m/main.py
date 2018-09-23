class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        i = 0
        cnt = 0
        max_seq_start = collections.defaultdict(int)
        while i < len(p):
            ii = i + 1
            while ii < len(p) and ord(p[ii]) - ord(p[ii - 1]) in [-25, 1]:
                ii += 1
            
            # Don't care about duplidates
            # cnt += (ii - i + 1) * (ii - i) / 2
            
            for j in range(i, ii):
                max_seq_start[p[j]] = max(max_seq_start[p[j]], ii - j)
            
            i = ii
            
        return sum(v for ch, v in max_seq_start.items())
    
# Store longest increasing string starting from char