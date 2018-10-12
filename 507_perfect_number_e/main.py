class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sumv = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sumv += i
                if num / i != i:
                    sumv += num / i
        return sumv == num

# Corner Test cases <= 0, 1
# Check if divisor != num line 11 and 13