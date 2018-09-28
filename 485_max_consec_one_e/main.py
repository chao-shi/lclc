class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        maxwin, win = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1 and (nums[i-1] == 0 or i == 0):
                win = 1
            elif nums[i] == 1:
                win += 1
            maxwin = max(maxwin, win)
        return maxwin

# Single loop