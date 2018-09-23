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
        while i < n1 * len(s1):
            ch1 = s1[i % len(s1)]
            ch2 = s2[j % len(s2)]
            if ch1 == ch2:
                i, j = i + 1, j + 1
            else:
                i += 1
        
        rep_s2 = j / len(s2)
        return rep_s2 / n2
        

# TLE