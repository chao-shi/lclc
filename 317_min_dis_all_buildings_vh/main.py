class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n  = len(grid), len(grid[0])
        distance_map = [[{} for i in range(n)] for j in range(m)]
        
        def bfs_span(i, j, label):
            q = collections.deque([(i, j, 0)])
            while q:
                x, y, depth = q.popleft()
                for v in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    xx, yy = x + v[0], y + v[1]
                    if 0 <= xx <  m and 0 <= yy < n and grid[xx][yy] == 0 and label not in distance_map[xx][yy]:
                        # single source so no need to compare depth as usual here
                        q.append((xx, yy, depth + 1))
                        distance_map[xx][yy][label] = depth + 1
        
        label = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs_span(i, j, label)
                    label += 1
                
        min_dis = sys.maxint
        for i in range(m):
            for j in range(n):
                if len(distance_map[i][j]) == label:
                    distance = sum(distance_map[i][j][l] for l in distance_map[i][j])
                    min_dis = min(min_dis, distance)
        
        return -1 if min_dis == sys.maxint else min_dis
                     