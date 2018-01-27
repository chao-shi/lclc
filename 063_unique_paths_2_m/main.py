class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        row = [1] + [0] * (n-1)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    row[j] = 0
                elif j > 0:
                    row[j] = row[j] + row[j-1]
                # no change for j = 0
        return row[-1]

# needs hidden row now