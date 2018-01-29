class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largestRectangleArea(heights):
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

        if not matrix or not matrix[0]:
            return 0

        maxv = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n

        for i in range(m):      
            for j in range(n):
                heights[j] = 0 if matrix[i][j] == '0' else heights[j] + 1
            maxv = max(maxv, largestRectangleArea(heights))
        return maxv

# 157ms