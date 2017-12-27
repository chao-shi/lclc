class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        for i in range(k):
            j = 0
            while j < len(num) - 1 and num[j] <= num[j+1]:
                j += 1
            num = num[:j] + num[j+1:]
        num = num.lstrip('0')
        if not num:
            return "0"
        return num