class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
    
# Case of [2,3,4,7]
# First all move to 7. +5 = max - min
# [7, 8, 9, 7]
# Then all move to 9. +2 = max_2 - min
# and so on
# the answer is sum(element - min)