class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
    
# Essentially Math.max(min1 * min2 * max1, max1 * max2 * max3);