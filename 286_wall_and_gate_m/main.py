class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        level = [(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0]
        distance = 0
        
        while level:
            new_level = []
            for coord in level:
                for v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y =coord[0] + v[0], coord[1] + v[1]
                    
                    if x < 0 or x == m or y < 0 or y == n or rooms[x][y] == -1:
                        continue
                    
                    if rooms[x][y] > distance + 1:
                        rooms[x][y] = distance + 1
                        new_level.append((x, y))

            level = new_level
            distance += 1
        
# The cool idea of initializing the queue with all gate and run only one BFS