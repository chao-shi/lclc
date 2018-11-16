class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # For example 8 A can be 
        # C, P, C, P, C, P 
        # or
        # C, P, C, P, P, P
        # We find that C + i * P will multiply the size by i + 1
        # If n is factorized into f1 * f2 * .. fn
        # Then the answer is f1 + f2 + ... fn
        # So our goal is to minimize the sum of factors
        # ab > a + b when a > 1 and b > 1
        # So always factor as much as possible
        res = 0
        factor = 2
        while n > 1:
            if n % factor == 0:
                n /= factor
                res += factor
            else:
                factor += 1
        return res