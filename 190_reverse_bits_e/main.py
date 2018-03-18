class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        ndigits = 0 
        while n > 0:
            ret <<= 1
            ret += n & 1
            n >>= 1
            ndigits += 1

        return ret << (32 - ndigits)

# Read the description carefully
