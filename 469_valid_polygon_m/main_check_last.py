class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # checking the edge vector if it is keeping moving clockwise or counter
        for i in range(len(points)):
            i1 = (i + 1) % len(points)
            i2 = (i1 + 1) % len(points)
            e1 = (points[i1][0] - points[i][0], points[i1][1] - points[i][1])
            e2 = (points[i2][0] - points[i1][0], points[i2][1] - points[i1][1])
            
            cross = e1[0] * e2[1] - e1[1] * e2[0]
            if cross == 0:
                continue

            if last_cross != None and last_cross * cross < 0:
                return False
            last_cross = cross
        return True

# Careful when two edges are same direction, line 18
# Cross product