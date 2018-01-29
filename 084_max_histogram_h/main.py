class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights + [0]
        stack = []
        maxv = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                maxv = max(maxv, heights[stack[-1]] * (i - stack[-2] - 1))
                stack.pop()
            stack.append(i)
        return maxv