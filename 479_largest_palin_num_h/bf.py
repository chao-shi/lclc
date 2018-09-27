class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def make_palin(num):
            return int(str(num) + str(num)[::-1])

        # Not very strict here
        # Kind of assume that n > 1 the result will be even digit number???
        if n == 1:
            return 9

        upper, lower = 10**n - 1, 10**(n-1)
        
        cand = upper
        while True:
            palin = make_palin(cand)
            # print palin
            for i in range(upper, max(lower, int(math.sqrt(palin))) - 1, -1):
                if palin % i == 0 and lower <= palin / i <= upper:
                    return palin % 1337
            cand -= 1
            
            