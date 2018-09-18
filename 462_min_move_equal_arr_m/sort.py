class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        ret = 0
        for i in range(len(nums) / 2):
            ret += nums[len(nums) - 1 - i] - nums[i]
        return ret
            