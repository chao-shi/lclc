class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(s, i, j):
            j -= 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1

        def squeeze(s):
            # squeeze space
            j = 0
            for i in range(len(s)):
                if s[i] != " " or (j > 0 and s[j-1] != " "):
                    s[j] = s[i]
                    j += 1
            # remove trailing space
            if j > 0 and s[j - 1] == " ":
                j -= 1
            return j

        s = str
        lens = squeeze(s)
        reverse(s, 0, lens)

        last_space = -1
        for i in range(lens + 1):
            if i == lens or s[i] == " ":
                reverse(s, last_space+1, i)
                last_space = i