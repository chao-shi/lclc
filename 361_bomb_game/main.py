class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        enermies = {}

        for i in range(n):
            row = grid[i]
            idxw = [-1] + [ii for ii, ch in enumerate(row) if ch == 'W'] + [m]

            for j in range(1, len(idxw)):
                cnt = row[idxw[j-1] + 1: idxw[j]].count('E')
                for k in range(idxw[j-1] + 1, idxw[j]):
                    if row[k] == '0':
                        enermies[(i, k)] = cnt
        
        maxv = 0

        for i in range(m):
            col = [grid[ii][i] for ii in range(n)]
            idxw = [-1] + [ii for ii, ch in enumerate(col) if ch == 'W'] + [n]

            for j in range(1, len(idxw)):
                cnt = col[idxw[j-1] + 1: idxw[j]].count('E')
                for k in range(idxw[j-1] + 1, idxw[j]):
                    if col[k] == '0':
                        enermies[(k, i)] = enermies.get((k, i), 0) + cnt
                        maxv = max(maxv, enermies[(k, i)], maxv)
                        
        return maxv