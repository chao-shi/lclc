class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i, num in enumerate(nums):
            if 0 < num <= len(nums):
                nums[j] = num
                j += 1
        
        for i in range(j, len(nums)):
            nums[i] = 1
        
        # Now partitioned nums
        # left | right
        # left side all nums in [1, n]
        # right side, all one (All out of range numbers removed)
        # this handle the case when there are negative numbers gracefully
        
        for i in range(j):
            v = nums[i] if nums[i] > 0 else -nums[i]
            if nums[v - 1] > 0:
                nums[v - 1] = - nums[v-1]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1

# Partitioning is better than previous swapping loop method. Complexity analysis is more clear