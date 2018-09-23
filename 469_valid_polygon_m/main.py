class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # checking the edge vector if it is keeping moving clockwise or counter
        crosses = []
        for i in range(len(points)):
            i1 = (i + 1) % len(points)
            i2 = (i1 + 1) % len(points)
            e1 = (points[i1][0] - points[i][0], points[i1][1] - points[i][1])
            e2 = (points[i2][0] - points[i1][0], points[i2][1] - points[i1][1])
            
            crosses.append(e1[0] * e2[1] - e1[1] * e2[0])
        return all(c >= 0 for c in crosses) or all(c <= 0 for c in crosses)