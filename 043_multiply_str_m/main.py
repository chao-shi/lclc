class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n, m = len(num1), len(num2)
        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                tmp = res[i+j+1] + int(num1[i]) * int(num2[j])
                res[i+j+1] = tmp % 10
                res[i+j] += tmp / 10
                # can be bigger than 10 here
                # will be smoothed by next round
                # Q: no need to worry about the most significant bit
                # because it is guaranteed no overflow
        
        res = "".join(map(str, res)).lstrip('0')
        if not res:
            return "0"
        return res