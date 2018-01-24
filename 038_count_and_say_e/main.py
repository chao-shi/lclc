class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for ii in range(n - 1):
            last = 0
            ss = ""
            for i in range(1, len(s)):
                if s[i] != s[last]:
                    ss += str(i - last) + s[last]
                    last = i
            # careful of the end
            s = ss + str(len(s) - last) + s[last]
        return s
            