class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Left increasing stack
        stack = [0]
        i = 1
        while i < len(nums) and nums[i] >= nums[i-1]:
            stack.append(i)
            i += 1
        
        for ii in range(i, len(nums)):
            while stack and nums[stack[-1]] > nums[ii]:
                stack.pop()
        
        # [lb, rb) needs resorting
        lb = stack[-1] + 1 if stack else 0
        
        # Right decreasing stack
        stack = [len(nums) - 1]
        i = len(nums) - 2
        while i >= 0 and nums[i] <= nums[i+1]:
            stack.append(i)
            i -= 1
        
        for ii in range(i, -1, -1):
            while stack and nums[stack[-1]] < nums[ii]:
                stack.pop()
                
        rb = stack[-1] if stack else len(nums)
        
        # Does not cover sorted case
        return max(0, rb - lb)
        
# My idea is same as solution 4