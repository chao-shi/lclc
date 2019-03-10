class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        i = 0
        anchor = 0
        max_seq_start = collections.defaultdict(int)
        for i in range(1, len(p) + 1):
            if i == len(p) or (ord(p[i]) - ord(p[i - 1]) not in [-25, 1]):
                for j in range(anchor, i):
                    max_seq_start[p[j]] = max(max_seq_start[p[j]], i - j)
                anchor = i
        return sum(v for ch, v in max_seq_start.items())
    
# Store longest increasing string starting from char