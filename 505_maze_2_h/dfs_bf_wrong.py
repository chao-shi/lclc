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
                    res.append((xx, yy, dirs[i]))
            return res
    

        def recur(x, y, steps):
            if [x, y] == destination:
                self.min_steps = min(self.min_steps, steps)
            elif (x, y) in visited:
                return
            else:
                visited.add((x, y))
                for cand in roll_4d(x, y):
                    recur(cand[0], cand[1], steps + abs(cand[0] - x) + abs(cand[1] - y))
                # visited.remove((x, y))

    
        m, n = len(maze), len(maze[0])
        self.min_steps = m * n + 1
        visited = set()
        
        if not wall_next(destination[0], destination[1]):
            return -1

        recur(start[0], start[1], 0)
        return self.min_steps if self.min_steps != m * n + 1 else -1

# A simple adaption of maze1 main.py
  
# Block 36, even (x, y) has been visited. But if it is different branch (not on the expanding path)
# We should still try it if the current branch can lead to shorter path. That's why it brings us
# the visited map storing the distance

# This approach we will only reach destination with the lexically smallest order (First branch everywhere)
# Destination will only be met once, not necessarily shortest distance

# DFS good for checking if reachable, that's why Maze 1 it works, not here


