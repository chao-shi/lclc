class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ret = 0
        for i, ch in enumerate(s):
            flag = 1
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                flag = -1
            ret += flag * m[ch]
        return ret
            
        