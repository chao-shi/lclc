class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != ' ':
                j += 1
            s[i:j] = s[i:j][::-1]
            i = j + 1
        return "".join(s)
        