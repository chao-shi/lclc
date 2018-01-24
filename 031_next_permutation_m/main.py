class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 2, 3, 3, 1, 1
        # j stops at index 0
        # i stops at index 2
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums[:] = nums[::-1]
            return

        j = i - 1
        i = len(nums) - 1
        while i >= 0 and nums[i] <= nums[j]:
            i -= 1
        
        nums[j], nums[i] = nums[i], nums[j]
        nums[j+1:] = nums[j+1:][::-1]

# Standard approach
# 1. search last element e[i] < e[i+1]
# 2. search last element j such that e[j] > e[i]
# 3. swap i, j element, this guarantee e[i+1:] is still descending. (Prove it)
# 4. reverse e[i+1:]

# Careful case line 14