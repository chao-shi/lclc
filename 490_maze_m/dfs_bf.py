class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])

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
            for v in vs:
                xx, yy = x, y
                while 0 <= xx < m and 0 <= yy < n and maze[xx][yy] == 0:
                    xx, yy = xx + v[0], yy + v[1]
                xx, yy = xx - v[0], yy - v[1]
                if (xx, yy) != (x, y):
                    res.append((xx, yy))
            return res

        visited = set()
        def recur(x, y):
            if x == destination[0] and y == destination[1]:
                return True
            # We have tried this branch, not working, return False
            # Actually two cases here
            # 1. x, y is on the current expanding path. Not necessarily (x, y) cannot reach 
            #    destination. But we don't care because we don't want to get into infinite loop
            # 2. x, y is on another previous branch. Then (x, y) must not be able to reach the destination
            #    because if it does, then the current branch won't even expand.
            elif (x, y) in visited:
                return False
            else:
                visited.add((x, y))
                for cand in roll_4d(x, y):
                    if recur(cand[0], cand[1]):
                        return True
                visited.remove((x, y))
                return False
                # Remove from visited 
                # Then we are enumerating all the paths, this will go exponentially
        
        # Pre-check quickly
        if not wall_next(destination[0], destination[1]):
            return False
        
        return recur(start[0], start[1])

# Theoretically correct, not exponential algorithm
        