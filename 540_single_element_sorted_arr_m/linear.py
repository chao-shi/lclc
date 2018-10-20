class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            if (i == 0 or nums[i-1] != num) and (i == len(nums) - 1 or nums[i+1] != num):
                return num
        
        