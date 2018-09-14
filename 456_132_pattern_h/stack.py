class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        min_left = [None]
        for i in range(len(nums)):
            new_min = nums[i] if min_left[-1] == None else min(min_left[-1], nums[i])
            min_left.append(new_min)

        stack = [0]
        
        for i in range(1, len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            if stack and stack[-1] > 0 and min_left[stack[-1]] < nums[i]:
                return True
            else:
                stack.append(i)
        
        return False
    
# Decreaseing sorted stack of "3"
# For each "3" we need to know what is the min "1" to the left
# New number is to check if it can be "2"

# Why decreasing of "3"
# If increasing. For example, we store [1, 3, 5]
# There is no need to have 3 here because 5 is larger
# 5 both have bigger range of numbers smaller
# Also have bigger choices of numbers on the left.
# So 3 can be removed. Then stack will always have 1 element. Not quite right.
# 
# How to further optimize. 
# Here we only try fix "1", "3" first and then find "2"
# what if we can fix "2", "3" first, this is solution of stack_opt.py
# 
# Fix 1, 2 first is the solution of merge_sort.py