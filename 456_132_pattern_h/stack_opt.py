class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max2 = None
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if max2 > nums[i]:
                return True

            while stack and stack[-1] < nums[i]:
                max2 = stack.pop()
            stack.append(nums[i])
        return False
            
# Fix "2" "3" and then find "1"
# The trick is no need to store "3"
# But we need to max out "2"
# To use a decreasing stack, every time an element is out of stack
# We know it matches pattern of "2" 
# Just need to maintain the larget of "2"