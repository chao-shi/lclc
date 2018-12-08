class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        max_len = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] > nums[j-1]:
                j += 1
            max_len = max(max_len, j - i)
            i = j
        return max_len
        
# Longest increasing array
        