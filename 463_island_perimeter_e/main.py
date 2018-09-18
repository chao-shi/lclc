class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (j == 0 or grid[i][j-1] == 0):
                    cnt += 2
                if grid[i][j] == 1 and (i == 0 or grid[i-1][j] == 0):
                    cnt += 2
        return cnt

# Like battleship problem