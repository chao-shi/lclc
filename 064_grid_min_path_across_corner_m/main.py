class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        row = grid[0][:]
        for i in range(1, n):
            row[i] += row[i-1]
        
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    row[j] += grid[i][j]
                else:
                    row[j] = grid[i][j] + min(row[j], row[j-1])
        return row[-1]