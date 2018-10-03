class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        hb = int(math.sqrt(area))
        for w in range(hb, 0, -1):
            if area % w == 0:
                return [area / w, w]