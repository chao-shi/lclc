class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        mt = {}
        for num in nums:
            while stack and stack[-1] < num:
                mt[stack.pop()] = num
            stack.append(num)
        return [mt.get(num, -1) for num in findNums]
            
            