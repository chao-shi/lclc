class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        m, n = len(grid), len(grid[0])

        def expand(i, j, dim):
            if i < 0 or i >=m or j < 0 or j >= n:
                return
            elif grid[i][j] == 0:
                return
            elif (i, j) in visited:
                return

            visited.add((i, j))
            dim[0] = min(dim[0], i)
            dim[1] = min(dim[1], j)
            dim[2] = max(dim[2], i)
            dim[3] = max(dim[3], j)

            for v in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ii, jj = i +v[0], j + v[1]
                expand(ii, jj, dim)
                
        
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dim = [i, j, i, j]
                    expand(i, j, dim)
                    island = tuple([tuple(grid[ii][dim[1]:dim[3]+1]) for ii in range(dim[0], dim[2] + 1)])
                    islands.add(island)
        return len(islands)

# Find the boundary of the island. However, the checking of line 35 is wrong.
# The following case failed

#101
#011
#110

#001
#011
#110

# same island is counted twice.