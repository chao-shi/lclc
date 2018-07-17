class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1
        # 9 (10 ^ 0 <= x < 10 ^ 1)
        # 10 * 9 - 9 = 9 * 9 (10 ^ 1 <= x < 10 ^ 2)
        # 10 * 9 * 8 - 9 * 8 = 9 * 9 * 8
        
        def pi(start, len):
            prod = 1
            for i in range(len):
                prod *= start
                start -= 1
            return prod

        cnt = 1
        for i in range(n):
            cnt += 9 * pi(9, i)
        return cnt