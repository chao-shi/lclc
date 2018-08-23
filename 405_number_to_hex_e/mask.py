class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Very smart, convert the number to unsigned
        # From unsigned to HEX
        num = num & 0xFFFFFFFF
        digits = list("0123456789abcdef")
        
        hex = ['0'] * 8
        for i in range(8):
            d = digits[num & 0xF]
            hex[7 - i] = d
            num >>= 4

        # Remove leading zeros
        i = 0
        while i < len(hex) and hex[i] == '0':
            i += 1
        return "".join(hex[i:]) if i < len(hex) else '0'

# I also thought about using the approach of converting to positive number first
# -1 is 0xFFFFFFFF, with first bit is 1, which is -2^31

# So if a number is negative, just + 2^31 (0x80000000), Find the hex representation
# of this number, for case of -1 it will be 0x7FFFFFFF
# 
# The problem is how we will do the merge. The first bit 1 may or may not add to the
# first hex
# 
# Lesson learned, any efforts going to base 10 is worthless.