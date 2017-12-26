class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            elif n == 3:
                n = 2
            elif (n + 1) % 4 == 0:
                # which way removes most 1 at one shot
                n += 1
            else:
                n -= 1
            step += 1
        return step
        
        