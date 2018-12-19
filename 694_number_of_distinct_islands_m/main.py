class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        m, n = len(grid), len(grid[0])

        def expand(i, j, i0, j0, island):
            if i < 0 or i >=m or j < 0 or j >= n:
                return
            elif grid[i][j] == 0:
                return
            elif (i, j) in visited:
                return

            visited.add((i, j))
            island.append((i-i0, j-j0))

            for v in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ii, jj = i +v[0], j + v[1]
                expand(ii, jj, i0, j0, island)
                
        
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    island = []
                    expand(i, j, i, j, island)
                    islands.add(tuple(island))
        return len(islands)
    
# The order of DFS is guaranteed