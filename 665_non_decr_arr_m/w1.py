class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len([i for i in range(1, len(nums)) if nums[i] < nums[i-1]]) <= 1

# Does not pass
# [3,4,2,3]