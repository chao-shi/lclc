class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])

        def inside(x, y):
            return 0 <= x < m and 0 <= y < n

        def bfs(x, y):
            q = collections.deque()
            q.append((x, y))
            depth = 1
            visited = set([(x, y)])

            while q:
                cur_len = len(q)
                for _ in range(cur_len):
                    x1, y1 = q.popleft()
                    for v in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        x2, y2 = x1 + v[0], y1 + v[1]
                        if not inside(x2, y2) or (x2, y2) in visited:
                            continue
                        elif matrix[x2][y2] == 0:
                            return depth
                        else:
                            visited.add((x2, y2))
                            q.append((x2, y2))
                depth += 1
                
                
        res = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    res[i][j] = bfs(i, j)
        return res
                            
                
# Passes OJ. I though about solving like maze shortest distance to exit first. 
# Maze problem has very few exits
# But not feasible with too many zeroes here