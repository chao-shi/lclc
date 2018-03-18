class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        a, b = 0, nums[0]
        for i in range(1, len(nums)):
            a, b= b, max(nums[i] + a, b)
        return b