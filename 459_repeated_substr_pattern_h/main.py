class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # idea try all lengths
        n = len(s)
        for k in range(1, n):
            if n % k == 0 and s[:k] * (n/k) == s:
                return True
        return False