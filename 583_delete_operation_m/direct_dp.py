class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        mt = {}
        m, n = len(word1), len(word2)
        
        for i in range(m+1):
            mt[(i, 0)] = i
        for j in range(n+1):
            mt[(0, j)] = j
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                ans = min(mt[(i-1, j)], mt[(i, j-1)]) + 1
                if word1[i-1] == word2[j-1]:
                    ans = min(ans, mt[(i-1, j-1)])
                mt[(i, j)] = ans
        return mt[(m, n)]                    
        