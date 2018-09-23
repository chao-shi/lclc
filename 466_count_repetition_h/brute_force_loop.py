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
        loop_i, loop_j = None, None
        while i < n1 * len(s1):
            if i % len(s1) == j % len(s2) == 0 and j > 0:
                mul = n1 * len(s1) / i
                i *= mul
                j *= mul
                
            ch1 = s1[i % len(s1)]
            ch2 = s2[j % len(s2)]
            if ch1 == ch2:
                i, j = i + 1, j + 1
            else:
                i += 1
            if i % 1000 == 0:
                print i
        
        rep_s2 = j / len(s2)
        return rep_s2 / n2

# Does not pass for case where no loop
# print Solution().getMaxRepetitions("phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjpre", 1000000,"pggxr", 100)