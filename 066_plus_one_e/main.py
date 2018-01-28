class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            res = digits[i] + c
            digits[i] = res % 10
            c = res / 10
            if c == 0:
                return digits
        if c == 1:
            digits.insert(0, 1)
        return digits