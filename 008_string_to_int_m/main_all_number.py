class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # group number are pre-order
        # group numbers are static. If ()? is absent, the group will be None
        # m = re.match(pattern, "134e45")
        # m.group(2) is None
        pattern = "^(0|-?[1-9][0-9]*)(\.[0-9]+)?(e-?[1-9][0-9]*)?$"
        m = re.match(pattern, str)
        
        if not m:
            return None
        
        integer = self.parseInteger(m.group(1))
        fraction = self.parseFraction(m.group(2))
        exponent = self.parseExponent(m.group(3))
        
        return (integer + fraction) * exponent
        
    
    def parseInteger(self, str):
        if str[0] == '-':
            flag = -1
            num = str[1:]
        else:
            flag = 1
            num = str
        ret = 0
        for i in range(len(num)):
            ret *= 10
            ret += int(num[i])
        return ret * flag

    def parseFraction(self, str):
        if not str:
            return 0
        e = 0.1
        ret = 0
        for i in range(1, len(str)):
            ret += int(str[i]) * e
            e /= 10
        return ret

    def parseExponent(self, str):
        if not str:
            return 1
        return 10 ** self.parseInteger(str[1:])
