class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not isVowel(s[i]):
                i += 1
            while i < j and not isVowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
        return "".join(s)

def isVowel(ch):
    return ch in "aeiouAEIOU"