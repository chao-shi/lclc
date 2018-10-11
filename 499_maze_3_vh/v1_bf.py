class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        m, n = len(maze), len(maze[0])
        hole = (hole[0], hole[1])

        def roll_4d(x, y):
            res = []
            vs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            dirs = "dlur"
            for i, v in enumerate(vs):
                xx, yy = x, y
                while 0 <= xx < m and 0 <= yy < n and maze[xx][yy] == 0 and (xx, yy) != hole:
                    xx, yy = xx + v[0], yy + v[1]
                if (xx, yy) != hole:
                    xx, yy = xx - v[0], yy - v[1]
                if (xx, yy) != (x, y):
                    res.append((xx, yy, dirs[i]))
            return res
        
        self.min_steps = m * n + 1
        self.operations = None
        visited = set()

        def recur(x, y, operations, steps):
            if (x, y) == hole:
                if steps < self.min_steps:
                    self.min_steps, self.operations = steps, operations
                elif steps == self.min_steps and operations < self.operations:
                    self.operations = operations
            elif (x, y) in visited:
                return
            else:
                visited.add((x, y))
                for cand in roll_4d(x, y):
                    recur(cand[0], cand[1], operations + cand[2], steps + abs(cand[0] - x) + abs(cand[1] - y))
                visited.remove((x, y))
        
        recur(ball[0], ball[1], "", 0)
        return self.operations if self.min_steps != m * n + 1 else "impossible"
                
# I first start without line 42
# Then the issue is that we may not have the optmial solution
# Let's say we first reach x, y from source through a roundabout way, and we reach hole from x, y
# We still need to evaluate later a shorter solution from source to x, y

# This approach is very slow. Smart pruning is done in v2.py
# 