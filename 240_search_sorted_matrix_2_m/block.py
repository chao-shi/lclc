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
        
        # x, y is the coordinate of bottom left
        def recur(x, y):
            if x >= m or y >= n:
                return False

            i = 0
            while i <= x and matrix[i][y] <= target:
                i += 1
            i -= 1
            
            # Don't forget here
            if i == -1:
                return False
            
            j = y
            while j < n and matrix[i][j] <= target:
                j += 1
            j -= 1
            
            # biggest element matrix[i][j] which is <= target
            if matrix[i][j] == target:
                return True
            return recur(i, j + 1)
        
        
        return recur(m-1, 0)
    
# Don't forget block 23
# Block approach, going towards top right