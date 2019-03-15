class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        res = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    res[i][j] = m * n + 1

        zeros = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]

        q = collections.deque()
        q.extend(zeros)
        
        while q:
            x, y = q.popleft()
            for v in [(0, 1), (1, 0), (0, -1),(-1, 0)]:
                xx, yy = x + v[0], y + v[1]
                if 0 <= xx < m and 0 <= yy < n and res[xx][yy] > res[x][y] + 1:
                    res[xx][yy] = res[x][y] + 1
                    q.append((xx, yy))
        return res

# Multiple start BFS.
# To avoid using visited variable few choices
# 1. Traverse layer by layer, each layer use set
# 2. Use the distance map, and only push to queue when strictly smaller found