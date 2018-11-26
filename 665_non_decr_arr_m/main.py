class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        drs = [i for i in range(1, len(nums)) if nums[i] < nums[i-1]]
        if len(drs) > 1:
            return False
        elif len(drs) == 0:
            return True
        else:
            i = drs[0]
            # Need to check if bring nums[i-1] down, does the relationship between nums[i-2] and 
            # nums[i-1] violates
            if i < 2 or nums[i-2] <= nums[i]:
                return True
            # Need to check if bring nums[i] up, does the relationship between nums[i] and 
            # nums[i+1] violates
            elif i == len(nums) - 1 or nums[i+1] >= nums[i-1]:
                return True
            else:
                return False
