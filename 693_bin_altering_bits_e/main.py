class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_str = bin(n)[2:]
        return all(bin_str[i] == '1' for i in range(0, len(bin_str), 2)) and all(bin_str[i] == '0' for i in range(1, len(bin_str), 2))