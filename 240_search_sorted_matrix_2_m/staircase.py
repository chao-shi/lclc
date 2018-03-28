class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False
    
# Key idea, I want to see which position of each row target will fit
# First thing come to mind is binary search for each row
# But once we search the first row
# the index of the target on the second row can only be to the left
# So here comes this staircase pointer approach.