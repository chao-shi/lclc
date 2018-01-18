class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i] = nums[j-1]
                j -= 1
        return j

# Good question