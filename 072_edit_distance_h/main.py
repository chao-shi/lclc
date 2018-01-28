class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            m[i][0] = m[i-1][0] + 1
        for i in range(1, len(word2) + 1):
            m[0][i] = m[0][i-1] + 1
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                m[i][j] = min(m[i-1][j], m[i][j-1], m[i-1][j-1]) + 1
                if word1[i-1] == word2[j-1]:
                    m[i][j] = min(m[i][j], m[i-1][j-1])
        return m[len(word1)][len(word2)]
            