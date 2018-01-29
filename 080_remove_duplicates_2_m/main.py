class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i, num in enumerate(nums):
            if j < 2 or not (nums[j - 1] == nums[j - 2] == num):
                nums[j] = num
                j += 1
        return j
                