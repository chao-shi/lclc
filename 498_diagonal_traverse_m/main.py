class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        
        def move(i, j, direction):
            if direction == 0:
                # Move up
                if i > 0 and j < n - 1:
                    return i - 1, j + 1, direction
                elif j == n - 1:
                    # Right edge (include top right corner)
                    return i + 1, j, 1 - direction
                else:
                    # Top edge (exclude top right corner)
                    return i, j + 1, 1 - direction
            else:
                if j > 0 and i < m - 1:
                    return i + 1, j - 1, direction
                elif i == m - 1:
                    # Bottom edge (include left bottom corner)
                    return i, j + 1, 1 - direction
                else:
                    # Left edge (exclude left bottom corner)
                    return i + 1, j, 1 - direction
                
        
        res = []
        i, j, direction = 0, 0, 0
        for _ in range(m * n):
            res.append(matrix[i][j])
            i, j, direction = move(i, j, direction)
        return res
    