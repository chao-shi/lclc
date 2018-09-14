class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g), sorted(s)
        i, j = 0, 0
        cnt = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cnt += 1
                i, j = i + 1, j + 1
            else:
                j += 1
        return cnt
                