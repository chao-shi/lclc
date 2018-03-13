class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # split() handles leading and ending space and multiple of them
        return " ".join(s.split()[::-1])