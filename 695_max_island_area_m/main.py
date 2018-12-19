class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        m, n = len(grid), len(grid[0])

        def expand(i, j):
            if i < 0 or i >=m or j < 0 or j >= n:
                return 0
            elif grid[i][j] == 0:
                return 0
            elif (i, j) in visited:
                return 0
            
            cnt = 1
            visited.add((i, j))

            for v in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ii, jj = i +v[0], j + v[1]
                cnt += expand(ii, jj)
            return cnt
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = expand(i, j)
                    max_area = max(max_area, area)
        return max_area
