class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(n))
        i = len(digits) - 1
        while i > 0 and digits[i] <= digits[i-1]:
            i -= 1
        
        if i == 0:
            return -1
        
        j = len(digits) - 1
        while j > 0 and digits[j] <= digits[i-1]:
            j -= 1
        digits[i-1], digits[j] = digits[j], digits[i-1]
        
        digits = digits[:i] + sorted(digits[i:])
        
        num = int("".join(digits))
        
        return num if num <= (1<< 31) - 1 else -1