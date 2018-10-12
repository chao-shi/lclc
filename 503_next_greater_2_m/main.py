class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        stack = []
        for _ in range(2):
            for i, num in enumerate(nums):
                while stack and nums[stack[-1]] < num:
                    res[stack.pop()] = num
                stack.append(i)
        return res