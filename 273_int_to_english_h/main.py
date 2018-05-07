class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        map_0_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"] + \
                ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        map_10s = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        def under_thousand(num):
            res = []
            h = num / 100
            if h > 0:
                res.extend([map_0_20[h], "Hundred"])
            tens = num % 100
            t, d = tens / 10, tens % 10
            if tens < 20:
                res.append(map_0_20[tens])
            else:
                res.extend([map_10s[t], map_0_20[d]])
            return res
        
        if num == 0:
            return "Zero"

        tmp = []
        for i in range(4):
            tmp.append(num % 1000)
            num /= 1000

        b, m, t, d = tmp[::-1]
        
        res = []
        if b > 0:
            res.extend(under_thousand(b) + ["Billion"])
        if m > 0:
            res.extend(under_thousand(m) + ["Million"])
        if t > 0:
            res.extend(under_thousand(t) + ["Thousand"])
        res.extend(under_thousand(d))
        
        return " ".join(res).replace("  ", " ").strip()
    
# Line 43, strip multiple internal double space