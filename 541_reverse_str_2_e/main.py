class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = []
        for i in range(0, len(s), 2*k):
            j = min(len(s), i + 2 * k)
            if j - i < k:
                res.append(s[i:j][::-1])
            else:
                res.append(s[i:i+k][::-1] + s[i+k:j])
        return "".join(res)
                
                
            