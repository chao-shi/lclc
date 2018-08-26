class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        length = 0
        odd_flag = False
        for ch in counter:
            f = counter.get(ch)
            length += f - f % 2
            if f % 2 == 1:
                odd_flag = True
        return length + (1 if odd_flag else 0)
        