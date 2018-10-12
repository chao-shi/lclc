class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return "-" + self.convertPos(-num)
        return self.convertPos(num)
        
    def convertPos(self, num):
        if num == 0:
            return "0"
        res = []
        while num > 0:
            res.append(str(num % 7))
            num /= 7
        return "".join(res[::-1])

# Careful case of "0"