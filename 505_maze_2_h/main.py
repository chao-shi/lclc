from Queue import PriorityQueue

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        def wall_next(x, y):
            if x == 0 or maze[x-1][y] == 1:
                return True
            elif x == m - 1 or maze[x+1][y] == 1:
                return True
            elif y == 0 or maze[x][y-1] == 1:
                return True
            elif y == n - 1 or maze[x][y+1] == 1:
                return True

        def roll_4d(x, y):
            res = []
            vs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            dirs = "dlur"
            for i, v in enumerate(vs):
                xx, yy = x, y
                while 0 <= xx < m and 0 <= yy < n and maze[xx][yy] == 0:
                    xx, yy = xx + v[0], yy + v[1]
                xx, yy = xx - v[0], yy - v[1]
                if (xx, yy) != (x, y):
                    res.append((xx, yy))
            return res

        m, n = len(maze), len(maze[0])
        
        if not wall_next(destination[0], destination[1]):
            return -1
        
        pq = PriorityQueue()
        pq.put((0, start[0], start[1]))
        visited = {}
        visited[(start[0], start[1])] = 0

        while pq.qsize() > 0:
            steps, x, y = pq.get()

            if (x, y) in visited and visited[(x, y)] < steps:
                # First remove stale data, similar to mark -1 when we update the priority
                continue
            
            if (x, y) == (destination[0], destination[1]):
                return steps

            # The overwriting part of Dijkstra algorithm
            for cand in roll_4d(x, y):
                new_steps = steps + abs(cand[0] - x) + abs(cand[1] - y)
                if visited.get(cand, m * n + 1) > new_steps:
                    pq.put((new_steps, ) + cand)
                    visited[cand] = new_steps
        return -1

# Dijkstra algorithm is used to calculate shortest path for weighted gragh.
# In this question, I'm skipping all the middle point where the ball cannot stop.
# So it is essentially a weighted graph. 
# Bellman ford or dijkstra algorithm should be considered.

# If we have to use BFS, then each node must be any point. Then the edge is always distance 
# 1, which makes it un-weighted graph