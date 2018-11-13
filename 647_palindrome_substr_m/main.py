class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i, j = 0, 0
        while j < len(s):
            p1, p2 = i, j
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                p1, p2 = p1 - 1, p2 + 1
            k = p2 - p1
            ans += k / 2
            if i == j:
                j += 1
            else:
                i += 1
        return ans
            