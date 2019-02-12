class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Feed of bit 0
        # ab: 00 -> 00 -> 00 -> 00
        # Feed of bit 1
        # ab: 00 -> 01 -> 10 -> 00
        
        # Don't forget 01 + 0 -> 01 and 10 + 0 -> 10
        a, b = 0, 0
        for c in nums:
            a, b = (~a & b & c | a & ~b & ~c), (~a & ~b & c | ~a & b & ~c) 
        return b

# Each bit use a to count
# case of 2, 2, 3, 2

# a: 00
# b: 00

# Read vertically
# For each bit we have 00 and 00, means no 1 encountered

# c: 10

# Now 
# a: 00
# b: 10

# c: 10

# a: 10
# b: 00

# c: 11

# Now:
# a: 00
# b: 01

# c: 10

# Now
# a: 00
# b: 11

# Returun b

# We need full state diagram