# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # Smart to use direction vector to determine where to turn
        self.d = 0
        dir_v = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        cleaned = set()

        def orient(i_1, j_1, i, j):
            v = (i_1 - i, j_1 - j)
            idx = dir_v.index(v)
            if (idx - self.d) % 4 == 1:
                robot.turnRight()
            elif (idx - self.d) % 4 == 2:
                robot.turnRight()
                robot.turnRight()
            elif (idx - self.d) % 4 == 3:
                robot.turnLeft()
            self.d = idx
        
        # Optimize here
        def gen_direction():
            # return [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            # Optimization makes orient only one operation 
            # no matter result of the wall
            return dir_v[self.d:] + dir_v[:self.d]

        # clean i, j, moved from i_prev, j_prev
        def recur(i, j, i_prev, j_prev):
            robot.clean()
            cleaned.add((i, j))
            for v in gen_direction():
                i_1, j_1 = i + v[0], j + v[1]
                if (i_1, j_1) not in cleaned:
                    orient(i_1, j_1, i, j)
                    if robot.move():
                        recur(i_1, j_1, i, j)
            orient(i_prev, j_prev, i, j)
            robot.move()
        
        robot.clean()
        recur(0, 1, 0, 0)
        recur(1, 0, 0, 0)
        recur(0, -1, 0, 0)
        recur(-1, 0, 0, 0)     
        
# Key point is to use the index, fit the orient function is very universal.
# This approach is very efficient

# Better than top voted solution. The top voted will go back and forth but only clean once.
# Case of corner
# 
#      1
# 0 -> 01
#      1
# Will go left.

# The turning is very efficient !!!! Check if yourself