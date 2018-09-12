class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            num = abs(nums[i])
            nums[num - 1] = -abs(nums[num - 1])
        
        ret = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i + 1)
        return ret