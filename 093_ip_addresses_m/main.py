class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = [[[] for j in range(5)] for i in range(len(s) + 1)]
        m[0][0].append("")
        
        for i in range(1, len(s) + 1):
            for j in range(1, 5):
                for k in range(max(0, i - 3), i):
                    num = int(s[k:i])
                    if num < 256 and not (s[k] == '0' and i - k > 1):
                        concat = "." if j < 4 else ""
                        m[i][j].extend(ip + s[k:i] + concat for ip in m[k][j-1])
        return m[len(s)][4]