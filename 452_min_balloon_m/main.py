class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points = sorted(points)
        cross_end = points[0][1]
        cnt_arrow = 0

        for j in range(1, len(points)):
            if points[j][0] <= cross_end:
                cross_end = min(points[j][1], cross_end)
            else:
                cross_end = points[j][1]
                cnt_arrow += 1
        return cnt_arrow + 1
                