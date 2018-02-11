class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Feed of bit 0
        # ab: 00 -> 10 -> 01 -> 00
        # Feed of bit 1
        # ab: 00 -> 01 -> 10 -> 00
        
        # Make sure b is same as feed bit when count is 1
        a, b = 0, 0
        for c in nums:
            a, b = (~a & ~b & ~c | ~a & b & c), (~a & ~b & c | a & ~b & ~c)
        return b