class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        m = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == j == 0:
                    m[i][j] = True
                    continue
                k = i + j
                matched = False
                if i > 0:
                    matched = matched or (s3[k - 1] == s1[i-1] and m[i-1][j])
                if j > 0:
                    matched = matched or (s3[k - 1] == s2[j-1] and m[i][j-1])
                m[i][j] = matched
        return m[len(s1)][len(s2)]