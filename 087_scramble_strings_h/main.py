class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # much better solution
        # Line 10 and line 18/20 can early prune a lot of branches
        if s1 == s2:
            return True

        if sort(s1) != sort(s2):
            return False

        n = len(s1)
        for i in range(1, n):
            if sort(s1[:i]) == sort(s2[:i]) and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            elif sort(s1[:i]) == sort(s2[n-i:]) and self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                return True
        return False
            
def sort(s):
    return "".join(sorted(s))

# sorted for string return a list of chars