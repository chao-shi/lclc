class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = [1]
        for i, ch in enumerate(s):
            cnt = 0
            if int(s[i]) > 0:
                cnt += res[-1]
            if i >= 1 and 26 >= int(s[i-1:i+1]) >= 10:
                cnt += res[-2]
            res.append(cnt)
        return res[-1]