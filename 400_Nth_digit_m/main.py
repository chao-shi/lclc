class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # lb, hb, digits
        # 1,   9,   1
        # 10,  99,  2
        # 100, 999, 3 ...
        lb, hb = 1, 9
        total = 0
        digits = 1
        
        while True:
            if n <= total + (hb - lb + 1) * digits :
                break
            total += (hb - lb + 1) * digits
            digits += 1
            lb, hb = hb + 1, hb * 10 + 9

        n -= total + 1
        
        target_num = n / digits + lb 
        return int(str(target_num)[n % digits])

# Math problem