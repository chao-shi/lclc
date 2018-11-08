class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10 ** 9 + 7
        res = [1]
        
        for i in range(len(s)):
            total = 0
            
            d1 = s[i]
            if d1 == "*":
                total += res[-1] * 9
            elif d1 != "0":
                total += res[-1]

            if i > 0:
                d2 = s[i-1:i+1]
                if d2 == "**":
                    # * can only be 1-9
                    total += res[-2] * 15
                elif d2[0] == "*":
                    total += res[-2] * (2 if d2[1] <= "6" else 1)
                elif d2[1] == "*":
                    mmap = {"1": 9, "2": 6}
                    total += res[-2] * (mmap.get(d2[0], 0))
                else:
                    d2 = int(d2)
                    if 10 <= d2 <= 26:
                        total += res[-2]
            res.append(total % mod)
        return res[-1]