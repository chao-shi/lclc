class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if j == 0 or nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j += 1
        return j
        