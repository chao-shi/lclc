# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        ret = 0
        for i in range(len(points)):
            tan_map = {}
            vert_cnt = 0
            base = 1
            for j in range(i):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    base += 1
                elif points[j].x == points[i].x:
                    vert_cnt += 1 
                else:
                    tan = float (points[j].y - points[i].y) / float(points[j].x - points[i].x)
                    tan_map[tan] = tan_map.get(tan, 0) + 1 
            ret = max(ret, max(tan_map.values() + [vert_cnt]) + base)
        return ret
                    
# Line 18, no need to iterate all, only up to i
# Careful case:
# infinite tan
# duplicated points