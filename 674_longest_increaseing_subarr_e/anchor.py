class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        anchor = 0
        max_len = 0
        for i in range(len(nums)):
            if i and nums[i] <= nums[i-1]:
                anchor = i
            max_len = max(max_len, i - anchor + 1)
        return max_len