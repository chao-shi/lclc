class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # longest common sub sequence (subsequence)
        mt = {}
        m, n = len(word1), len(word2)
        
        for i in range(m+1):
            mt[(i, 0)] = 0
        for j in range(n+1):
            mt[(0, j)] = 0
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                ans = max(mt[(i-1, j)], mt[(i, j-1)])
                if word1[i-1] == word2[j-1]:
                    ans = max(ans, mt[(i-1, j-1)] + 1)
                mt[(i, j)] = ans
        
        common_seq_len = mt[(m, n)]
        return m + n - 2 * common_seq_len
                    
        