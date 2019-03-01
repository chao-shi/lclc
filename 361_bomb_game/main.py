class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        e_cnt = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for start, end, diff in [(0, n, 1), (n-1, -1, -1)]:
                cnt = 0
                for j in range(start, end, diff):
                    if grid[i][j] == 'W':
                        cnt = 0
                    elif grid[i][j] == 'E':
                        cnt += 1
                    else:
                        e_cnt[i][j] += cnt
        
        for j in range(n):
            for start, end, diff in [(0, m, 1), (m-1, -1, -1)]:
                cnt = 0
                for i in range(start, end, diff):
                    if grid[i][j] == 'W':
                        cnt = 0
                    elif grid[i][j] == 'E':
                        cnt += 1
                    else:
                        e_cnt[i][j] += cnt
        return max(map(max, e_cnt))