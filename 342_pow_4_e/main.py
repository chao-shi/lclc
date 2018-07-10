class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num&(num-1) == 0 and num&0x55555555 > 0
    
# num > 0 and num&(num-1) == 0 tells us only one 1 digit, check where is that digit 
# Don't forget 1 is also power of 4