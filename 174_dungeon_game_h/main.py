class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return None
        m, n = len(dungeon), len(dungeon[0])
        matrix = [[sys.maxint] * n for i in range(m)]
        matrix[-1][-1] = max(1, 1 - dungeon[-1][-1])
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m - 1:
                    matrix[i][j] = min(matrix[i][j], matrix[i + 1][j] - dungeon[i][j])
                if j < n - 1:
                    matrix[i][j] = min(matrix[i][j], matrix[i][j + 1] - dungeon[i][j])
                matrix[i][j] = max(1, matrix[i][j])
        return matrix[0][0]

# Sys.maxint needed, because we are using min here

# To go forward iteration. Needs to store two elements
# H(i, j) = (min_blood_needed_to_begin, blood_left_at_here)