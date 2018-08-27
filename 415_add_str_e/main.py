class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry > 0:
            sum = carry
            if i >= 0:
                sum += int(num1[i])
            if j >= 0:
                sum += int(num2[j])
            d, carry = sum % 10, sum / 10
            res.append(str(d))
            i, j = i - 1, j - 1

        return "".join(res[::-1])
        