class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Just to pass OJ "aaaaaaa...."
        if s == s[::-1]:
            return len(s)

        mt = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s)):
            mt[i][i+1] = 1

        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                j = i + l
                max_v = max(mt[i+1][j], mt[i][j-1])
                if s[j-1] == s[i]:
                    max_v = max(max_v, mt[i+1][j-1] + 2)
                mt[i][j] = max_v
        
        return mt[0][len(s)]
        
# No better solutions