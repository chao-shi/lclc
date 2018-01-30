class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        m = [1]
        for i, ch in enumerate(s):
            cnt = 0
            if ch != '0':
                cnt += m[-1]
            if ch <= '6' and i > 0 and s[i-1] == "2":
                cnt += m[-2]
            elif i > 0 and s[i-1] == "1":
                cnt += m[-2]
            m.append(cnt)
        return m[-1]