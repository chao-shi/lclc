class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j, num in enumerate(nums):
            if num != 0:
                nums[i] = num
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0

# Don't swap, populate zero at the end.

# Further optmization can happen at block 9
# if num != 0:
#   if j != i:
#        nums[i] = num
#   i += 1