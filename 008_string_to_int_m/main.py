class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # clean
        str = str.strip()
        i = 0
        while i < len(str) and (str[i].isdigit() or str[i] in '-+'):
            i += 1
        str = str[:i]

        pattern = "^(0|[+|-]?[0-9]+)$"
        m = re.match(pattern, str)
        
        if not m:
            return 0
        
        value = self.parseInteger(m.group(1))        
        if value > (1 << 31) - 1:
            return (1 << 31) - 1
        elif value < -(1 << 31):
            return - 1 << 31
        return value

    def parseInteger(self, str):
        if str[0] == '-':
            flag = -1
            num = str[1:]
        elif str[0] == '+':
            flag = 1
            num = str[1:]
        else:
            flag = 1
            num = str
        ret = 0
        for i in range(len(num)):
            ret *= 10
            ret += int(num[i])
        return ret * flag
    
# Bad points to make OJ happy
# need input clean " -0012a42"
# leading zero is valid, line 14 change
# +2 is valid, line 14 change
# return 0 if not matching, example is "+"
# return withint 32-bit integer range
# Very bad question